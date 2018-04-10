using UnityEngine;
using System.Collections;

public class Test : MonoBehaviour
{
	public Sprite texture; 

	// Use this for initialization
	void Start ()
	{
		texture.texture.GetPixel (0, 0);
	}
	
	// Update is called once per frame
	void Update () {
	
	}
}
