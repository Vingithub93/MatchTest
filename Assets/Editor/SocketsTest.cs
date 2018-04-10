using System;
using UnityEngine;
using System.Collections;
using System.Net;
using System.Net.Sockets;
using UnityEditor;

[InitializeOnLoad]
public class SocketsTest
{
    private static SocketsTest instance;

    private Socket clientSocket;
    private TcpListener listener;

    private byte[] resultBuffer;

    static SocketsTest()
    {
        instance = new SocketsTest();
    }

    //[MenuItem("Sockets/Listen")]
    public static void StartListening ()
    {
        instance.listener.Start();
        instance.listener.BeginAcceptSocket(instance.AcceptSocket, instance.listener);

        Debug.Log("Started listening for connections...");
    }

    //[MenuItem("Sockets/Stop")]
    public static void StopListening ()
    {
        instance.listener.Stop();
        if (instance.clientSocket != null) {
            instance.clientSocket.Close();
        }

        Debug.Log("Listening stopped");
    }

    private void AcceptSocket(IAsyncResult ar)
    {
        if (ar.IsCompleted) {
            Debug.Log("Connection established!");

            clientSocket = instance.listener.EndAcceptSocket(ar);
            resultBuffer = new byte[1024];
            BeginReceiveData();
        } else {
            Debug.Log("Connection canceled");
        }
}

    private void BeginReceiveData()
    {
        clientSocket.BeginReceive(resultBuffer, 0, resultBuffer.Length, SocketFlags.None, EndReceiveData, null);
    }

    private void EndReceiveData(IAsyncResult ar)
    {
        int bytesReceived = clientSocket.EndReceive(ar);
        Debug.Log(ProcessData(bytesReceived));

        BeginReceiveData();
    }

    private string ProcessData(int bytesReceived)
    {
        return System.Text.Encoding.UTF8.GetString(resultBuffer, 0, bytesReceived);
    }

    private SocketsTest ()
    {
        listener = new TcpListener(IPAddress.Any, 10000);
    }
}
