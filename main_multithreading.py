import Peer
import multiprocessing
import socket
import time
import identity
import Peer_utils


#initialize two peers
#start peer1 listening socket in a separate process
def peer1stuff(peer1):
        # peer1.send_message(f"peer_5002","Hello from Peer 1")
        # peer1.listen_for_broadcasts(6000)

        # peer1.start_listening_threads()
        # time.sleep(2)  # Give peer2 time to start listening
        # peer1.broadcast_new_peer_request('127.0.0.1', 9999, f"NEW_PEER_REQUEST:{peer1.peer_id}")
        # time.sleep(5)
        # peer1.broadcast_new_peer_request('127.0.0.1', 9999, "Another broadcast")

        peer1.start()

        



#start peer2 listening socket in a separate process
def peer2stuff(peer2):
        # peer2.start_listening_threads()
        # time.sleep(10)  # Keep process alive to receive broadcasts

        # print("now sending connection request from peer2 to peer1")
        #RESOURCE DISCOVERY FIRST
        #HEARING FOR BROADCAST REQUESTS

        # peer2.send_connection_request('127.0.0.1', 5001)
        # peer2.send_message(f"peer_5001","Hello from Peer 2")
        # peer2.receive_message(f"peer_5001")
        # peer2.broadcast_new_peer_request('255.255.255.255', 6000, "New peer joined the network")

        peer2.start()

#start peer2 listening socket in a separate process
def peer3stuff(peer3):
        # peer2.start_listening_threads()
        # time.sleep(10)  # Keep process alive to receive broadcasts

        # print("now sending connection request from peer2 to peer1")
        #RESOURCE DISCOVERY FIRST
        #HEARING FOR BROADCAST REQUESTS

        # peer2.send_connection_request('127.0.0.1', 5001)
        # peer2.send_message(f"peer_5001","Hello from Peer 2")
        # peer2.receive_message(f"peer_5001")
        # peer2.broadcast_new_peer_request('255.255.255.255', 6000, "New peer joined the network")

        peer3.start()

if __name__ == '__main__':
    
    path1 = "peer1_identity/peer1_identity.txt"
    peer_id1 = identity.load_or_generate_peer_id(PEER_ID_FILE=path1)
    peer1address = Peer_utils.get_local_ip()
    peer1port = Peer_utils.get_free_port()
    peer1 = Peer.Peer(peer_id=peer_id1, address=peer1address, port=peer1port)

    path2 = "peer2_identity/peer2_identity.txt"
    peer_id2 = identity.load_or_generate_peer_id(PEER_ID_FILE=path2)
    peer2address = Peer_utils.get_local_ip()
    peer2port = Peer_utils.get_free_port()
    peer2 = Peer.Peer(peer_id=peer_id2, address=peer2address, port=peer2port)

    path3 = "peer3_identity/peer3_identity.txt"
    peer_id3 = identity.load_or_generate_peer_id(PEER_ID_FILE=path3)
    peer3address = Peer_utils.get_local_ip()
    peer3port = Peer_utils.get_free_port()
    peer3 = Peer.Peer(peer_id=peer_id3, address=peer3address, port=peer3port)

    process1 = multiprocessing.Process(target=peer1stuff,args=(peer1,))
    process2 = multiprocessing.Process(target=peer2stuff,args=(peer2,))
    process3 = multiprocessing.Process(target=peer3stuff,args=(peer3,))

    process2.start()
#     time.sleep(5)  # Ensure peer2 starts before peer1
    process1.start()
#     time.sleep(5)  # Ensure peer1 starts before peer3
    process3.start()



    process2.join()
    process1.join()
    process3.join()

    


    

    
    