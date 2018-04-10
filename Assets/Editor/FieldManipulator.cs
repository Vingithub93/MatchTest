using System.Collections.Generic;
using System.Linq;
using MMKCore;
using UnityEditor;
using UnityEngine;
using UnityEngine.SceneManagement;

public class FieldManipulator : EditorWindow
{
    private readonly Dictionary<Sprite, Texture2D> spritesToTextures = new Dictionary<Sprite, Texture2D>();

    private Sprite[] sprites;
    private string[] attachmentNames;

    private string currentAttachment;
    private bool pressed;

    private void OnEnable ()
    {
        var prefabs = Resources.LoadAll<GameObject>(Constants.AttachmentsFolder);
        attachmentNames = prefabs.Select(prefab => prefab.name).ToArray();
        sprites = new Sprite[prefabs.Length];
        for (int i = 0; i < prefabs.Length; i++) {
            sprites[i] = prefabs[i].HasComponent<MMKCore.TokenComponents.Graphics>()
                ? prefabs[i].GetComponent<MMKCore.TokenComponents.Graphics>().Sprite
                : null;
            if (sprites[i] != null) {
                spritesToTextures[sprites[i]] = EditorUtilites.FetchTexture(sprites[i]);
            }
        }
        EditorApplication.update += Track;
    }

    private void OnGUI ()
    {
        if (SceneManager.GetActiveScene().name != Constants.MainGameScene) {
            return;
        }

        EditorGUILayout.BeginHorizontal();
        for (int i = 0; i < attachmentNames.Length; i++) {
            var sprite = sprites[i];
            var texture = sprite != null && spritesToTextures.ContainsKey(sprite) ? spritesToTextures[sprite] : null;

            if (GUILayout.Button(texture, GUILayout.Width(50f), GUILayout.Height(50f))) {
                pressed = true;
                currentAttachment = attachmentNames[i];
            }
        }
        EditorGUILayout.EndHorizontal();

        if (pressed) {
            EditorGUILayout.HelpBox("Currently in edit mode. Press RMB to exit", MessageType.Info);
        }
    }

    private void OnDestroy ()
    {
        EditorApplication.update -= Track;
    }

    private void Track ()
    {
        if (!pressed) {
            return;
        }

        if (Input.GetMouseButtonDown(1)) {
            pressed = false;
            Repaint();
            return;
        }

        if (!Input.GetMouseButtonDown(0)) {
            return;
        }

        var hit = Physics2D.Raycast(Camera.main.ScreenToWorldPoint(Input.mousePosition), Vector2.zero);

        if (hit.collider == null) {
            return;
        }

        ElementFactory.Attach(hit.collider.gameObject, currentAttachment);
    }
}
