import Peer
import multiprocessing
import socket
import time
import identity


if __name__ == '__main__':
    
    path1 = "peer1_identity/peer1_identity.txt"
    peer_id1 = identity.load_or_generate_peer_id(PEER_ID_FILE=path1)
    peer1 = Peer.Peer(peer_id=peer_id1, address='127.0.0.1', port=5001)
    peer1.broadcast_new_peer_request('192.168.0.255',9999)

    



    


    

    
    