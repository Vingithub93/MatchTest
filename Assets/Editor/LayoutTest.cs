using UnityEngine;
using System.Collections;
using UnityEditor;

public class LayoutTest : EditorWindow
{
    [MenuItem("Test/Layout")]
    public static void Init ()
    {
        var window = GetWindow<LayoutTest>();
        window.ShowUtility();
    }

    private Vector2 scrollPosition;
    private GUIStyle pressedButton;
    private GUIContent[] contents;
    private int selectedIndex;
    private bool toggleValue;

    private void OnEnable ()
    {
        contents = new[] {
            new GUIContent("First"),
            new GUIContent("Second"),
            new GUIContent("Third"),
            new GUIContent("Fourth"),
        };

        //foreach (var lvl in Resources.LoadAll<PremadeLevel>(Constants.LevelsFolder)) {
        //    lvl.chessBackground = false;
        //    EditorUtility.SetDirty(lvl);
        //}
        //AssetDatabase.SaveAssets();
    }

    private void OnGUI ()
    {
        EditorGUILayout.BeginHorizontal();
        {
            EditorGUILayout.BeginVertical();

            selectedIndex = GUILayout.SelectionGrid(selectedIndex, contents, 1, GUILayout.Height(100f));

            GUILayout.FlexibleSpace();

            GUILayout.Box("This is a tooltip", GUILayout.Height(150f), GUILayout.Width(300f));
            EditorGUILayout.EndVertical();

            EditorGUILayout.BeginVertical();
            EditorGUILayout.IntField("Integer field", 4);
            EditorGUILayout.LabelField("Text here");

            var defaultColor = GUI.color;
            GUI.color = Color.red;
            EditorGUILayout.BeginHorizontal();
            GUILayout.FlexibleSpace();
            GUILayout.Button("Text");
            GUILayout.FlexibleSpace();
            EditorGUILayout.EndHorizontal();
            GUI.color = defaultColor;

            toggleValue = GUILayout.Toggle(toggleValue, "Toggle",  GUI.skin.button, GUILayout.Width(50f), GUILayout.Height(50f));

            GUILayout.FlexibleSpace();

            EditorGUILayout.BeginHorizontal();
            GUILayout.FlexibleSpace();
            GUILayout.Button("First");
            GUILayout.Button("Second");
            EditorGUILayout.EndHorizontal();

            EditorGUILayout.EndVertical();
        }
        EditorGUILayout.EndHorizontal();
    }
}
