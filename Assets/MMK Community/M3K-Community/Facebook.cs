using System;
using UnityEngine;
using System.Collections;
using System.Collections.Generic;
using Facebook.Unity;
using UnityEngine.UI;


namespace MMKCore.Socials
{
    public class Facebook : MonoBehaviour, ISocialNetwork
    {
        private FacebookUI uiElement;

        private void Awake ()
        {
            var player = FindObjectOfType<Player>();
            if (player != null) {
                player.Social = this;
            }

            Init();
			InitFacebookUI ();
        }

		private void OnLevelWasLoaded (int level)
        {
			InitFacebookUI ();
        }

		void InitFacebookUI ()
		{
			uiElement = FindObjectOfType<FacebookUI> ();
			if (uiElement == null) {
				Debug.Log ("No Facebook UI object was found on this scene. Make sure that the Facebook UI script is attached and the game object is enabled");
			}
		}

        public void Init ()
        {
            if (!FB.IsInitialized) {
                FB.Init(SetupInit, OnHideUnity);
            } else {
                FB.ActivateApp();
            }
        }

        private bool isLoggedIn;

        public bool Login ()
        {
            try {
                List<string> permissions = new List<string> { "public_profile" };

                FB.LogInWithReadPermissions(permissions, AuthCallback);
                if (uiElement != null) {
                    uiElement.Connect();
                }
                
                return isLoggedIn;
            } catch (Exception e) {
                Debug.LogFormat("Exception while logging in to Facebook: {0}", e);
                return false;
            }
        }

        public void GetFriendList ()
        {
        }

        public void ShareProgress ()
        {
        }

        public void SaveProgress ()
        {
        }

        public void LoadProgress ()
        {
        }

        private void OnHideUnity (bool isGameShown)
        {
            Time.timeScale = isGameShown ? 1 : 0;
        }

        private void SetupInit ()
        {
            if (FB.IsInitialized) {
                FB.ActivateApp();
            }
        }

        private void AuthCallback (ILoginResult result)
        {
			if (result.Error != null) {
				Debug.LogFormat ("Error while logging in: {0}", result.Error);
			}

			Debug.Log (FB.IsLoggedIn ? "Facebook logged in successfully" : "Facebook wasn't logged in");

            isLoggedIn = FB.IsLoggedIn;
        }
    }
}


