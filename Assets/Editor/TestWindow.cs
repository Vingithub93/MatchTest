using System.Collections.Generic;
using UnityEngine;
using UnityEditor;
using UnityEditorInternal;

public class TestWindow : EditorWindow
{
    private ReorderableList list;

    [MenuItem("Window/Test")]
    public static void Open ()
    {
        GetWindow<TestWindow>();
    }

    private void OnEnable ()
    {
        list = new ReorderableList(new List<string>(), typeof (string), false, false, true, true);
        list.onRemoveCallback += reorderableList => {
            ReorderableList.defaultBehaviours.DoRemoveButton(reorderableList);
        };
        list.drawElementCallback += (rect, index, active, focused) => {
            list.list[index] = EditorGUI.TextField(rect, (string) list.list[index]);
        };
    }

    private void OnGUI ()
    {
        list.DoLayoutList();
    }
}
