using System;
using UnityEngine;
using System.Collections;
using System.Collections.Generic;
using MMKCore;
using MMKCore.TokenComponents;
using UnityEditor;
using UnityEngine.SceneManagement;

public class FieldDebug : EditorWindow
{
    [MenuItem("Window/Cheat panel", false, 5)]
    public static void Open ()
    {
        GetWindow<FieldDebug>();
        GetWindow<FieldManipulator>(typeof (FieldDebug));
    }
   
    private ITokensCollection Tokens
    {
        get { return ElementComponent.Tokens; }
    }

    private const float Size = 50f;
    private Dictionary<Sprite, Texture2D> spritesToTextures; 

    private Texture2D GetTexture (Sprite sprite)
    {
        if (sprite == null) {
            return null;
        }

        if (spritesToTextures.ContainsKey(sprite)) {
            return spritesToTextures[sprite];
        }

        var texture = EditorUtilites.FetchTexture(sprite);
        spritesToTextures.Add(sprite, texture);
        return texture;
    }

    private void OnEnable ()
    {
        Durability.OnTokenDestroyed += DurabilityOnOnTokenDestroyed;
        ShapesManager.OnCollapsingFinish += Repaint;
    }

    private void DurabilityOnOnTokenDestroyed(TokenColor color, PositionInfo info, IDamageDealer dealer)
    {
        Repaint();
    }

    private void OnGUI ()
    {
        if (SceneManager.GetActiveScene().name != Constants.MainGameScene || !EditorApplication.isPlaying) {
            spritesToTextures = null;
            return;
        }

        if (spritesToTextures == null) {
            spritesToTextures = new Dictionary<Sprite, Texture2D>();
        }

        for (int row = LevelConfig.rows - 1; row >= 0; row--) {
            EditorGUILayout.BeginHorizontal();
            for (int column = 0; column < LevelConfig.columns; column++) {
                var position = new PositionInfo(row, column);
                var token = Tokens[position];
                var sprite = token != null ? token.GetComponent<SpriteRenderer>().sprite : null;
                var texture = GetTexture(sprite);

                if (token != null
                    ? GUILayout.Button(texture, GUILayout.Width(Size), GUILayout.Height(Size))
                    : GUILayout.Button("Null", GUILayout.Width(Size), GUILayout.Height(Size))) {
                    Click(position);
                }
            }
            EditorGUILayout.EndHorizontal();
        }
    }

    private void Click (PositionInfo position)
    {
        EditorGUIUtility.PingObject(Tokens[position]);
        Selection.activeGameObject = Tokens[position];

        Debug.LogFormat("Supposed position: {0}, actual position: {1}",
            position.Coordinates(Level.Current.Builder.FieldOrigin), Tokens[position].transform.position);
    }

    private void OnDestroy ()
    {
        Durability.OnTokenDestroyed -= DurabilityOnOnTokenDestroyed;
        ShapesManager.OnCollapsingFinish -= Repaint;
    }
}
