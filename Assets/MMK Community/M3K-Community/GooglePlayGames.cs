#if UNITY_ANDROID
using System;
using GooglePlayGames;
using GooglePlayGames.BasicApi;
using GooglePlayGames.BasicApi.SavedGame;

using UnityEngine;

namespace MMKCore.Publishers
{
    public class GooglePlayGames : MonoBehaviour, IPublisher
    {
        private ISavedGameMetadata savedMetadata;
        private DateTime playStart;
        private string fileName = "googlePlaySavedGame.game";

        private bool loaded;

        public void Init()
        {
            var config = new PlayGamesClientConfiguration.Builder()
                .EnableSavedGames()
                .Build();

            PlayGamesPlatform.InitializeInstance(config);
            PlayGamesPlatform.DebugLogEnabled = true;
            PlayGamesPlatform.Activate()
                .Authenticate(AuthCallback);
        }

        public void Login()
        {
            if (!Social.localUser.authenticated) {
                Social.localUser.Authenticate(AuthCallback);
            }
        }

        private void AuthCallback (bool success)
        {
            if (success) {
                OpenSavedGame();
            }
        }

        public void SaveGame()
        {
			Debug.Log ("==== ATTEMPTING TO SAVE GAME TO CLOUD ====");
			if (savedMetadata != null && !savedMetadata.IsOpen) {
				OpenSavedGame ();
				return;
			}

			Debug.Log ("==== SAVING GAME TO CLOUD ====");

            var lastCompletedLevel = GameController.LastCompletedLevel;
            var description = lastCompletedLevel != 0
                ? string.Format("Last completed level {0}", lastCompletedLevel)
                : "No levels are completed";

            var gameClient = PlayGamesPlatform.Instance.SavedGame;
            var metadataUpdate = new SavedGameMetadataUpdate.Builder()
                .WithUpdatedDescription(description)
                .WithUpdatedPlayedTime(DateTime.Now.Subtract(playStart))
                .Build();

            if (gameClient != null) {
                gameClient.CommitUpdate(savedMetadata, metadataUpdate, GameController.GameBynary, SavingCallback);
            }
        }

        private void SavingCallback(SavedGameRequestStatus savedGameRequestStatus, ISavedGameMetadata savedGameMetadata)
        {
            savedMetadata = savedGameMetadata;
        }

        public void LoadGame()
        {
            if (loaded) {
                return;
            }

            Debug.Log("======== LOADING DATA FROM CLOUD ===========");
            var client = PlayGamesPlatform.Instance.SavedGame;
            client.ReadBinaryData(savedMetadata, LoadingCallback);
            loaded = true;
        }

        private void LoadingCallback(SavedGameRequestStatus savedGameRequestStatus, byte[] bytes)
        {
			if (savedGameRequestStatus == SavedGameRequestStatus.Success && bytes.Length != 0) {
                GameController.LoadFromByteData(bytes);
            } else {
                GameController.LoadFromFile();
            }
        }

        private void Awake ()
        {
			if (!Utilites.InternetAvailable) {
				return;
			}

            playStart = DateTime.Now;

            var player = FindObjectOfType<Player>();
            if (player != null) {
                player.Publisher = this;
            }

            Init();
            Login();

        }

        private void OpenSavedGame ()
        {
			Debug.Log ("==== OPENING SAVED GAME ====");
            var client = PlayGamesPlatform.Instance.SavedGame;
            client.OpenWithAutomaticConflictResolution(fileName, DataSource.ReadCacheOrNetwork, ConflictResolutionStrategy.UseLongestPlaytime, OpeningCallback);
        }

        private void OpeningCallback(SavedGameRequestStatus savedGameRequestStatus, ISavedGameMetadata savedGameMetadata)
        {
            if (savedGameRequestStatus == SavedGameRequestStatus.Success) {
                savedMetadata = savedGameMetadata;
				if (!loaded) {
					LoadGame ();
				} else {
					SaveGame ();
				}
            } else {

            }
        }
    }
}

#endif
