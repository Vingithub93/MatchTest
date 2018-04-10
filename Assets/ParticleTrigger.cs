using UnityEngine;
using System.Collections;

public class ParticleTrigger : MonoBehaviour
{
    public ParticleSystem particles;
    public float particlesDelay;

    private Animator animator;

	void Start ()
	{
	    animator = GetComponent<Animator>();
	    animator.SetTrigger("Trigger");
	    StartCoroutine(Particles());
	}

    private IEnumerator Particles ()
    {
        yield return new WaitForSeconds(particlesDelay);
        particles.Play();
    }
}
