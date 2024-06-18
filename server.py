import os
import socket, threading
import json
import time



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(("0.0.0.0", 1997))
s.listen()
clients = {}
addresses = {}

print("Jserver est pret...")
serverRunning = True


def handle_client(conn):
    try:
            data = conn.recv(1024).decode('utf8')
            newConnexion = '%s' % data
            print(data)
            clients[conn] = data.replace("___UserName___",'')
            try:
                for sock in clients:
                    print(clients[sock])

                    if clients[sock] == "JABTECHSERVER":
                        sock.send((data.replace("___UserName___",'')+"___UserName___").encode())
            except Exception as e:
                print(e)
            print(str(data)+" est en ligne")


            while True:

                try:
                    response = conn.recv(1024)
                    print(response.decode('utf-8') )

                    try:
                        if ("____çAutorisationç____" in response.decode('utf-8') ):
                            envoi= (response.decode('utf-8')).split("&&&&&&&&&&&&&&&&&&&&")



                            try:
                                for sock in clients:
                                    print(clients[sock])
                                    print(str(clients[sock])+" == "+str(envoi[-1]))
                                    if str(clients[sock]) == str(envoi[-1]):
                                        rep=response.decode('utf-8')
                                        rep = rep.replace("____çAutorisationç____","")
                                        sock.send(rep.encode())
                                        print("ENVOYER"+rep.encode())
                            except Exception as e:
                                print(e)

                        elif ("&&&&&&&&&&&&&&&&&&&&" in response.decode('utf-8') ):

                            try:
                                for sock in clients:
                                    print(clients[sock])

                                    if clients[sock] == "JABTECHSERVER":
                                        sock.send(response)
                            except Exception as e:
                                print(e)

                        elif ("yyyyyttttt" in response.decode('utf-8') ):

                            envoi = (response.decode('utf-8')).split("yyyyyttttt" )

                            try:
                                for sock in clients:
                                    print(clients[sock])
                                    print(str(clients[sock]) + " == " + str(envoi[0]))
                                    if str(clients[sock]) == str(envoi[0]):
                                        rep = response.decode('utf-8')
                                        rep = rep.replace(str(envoi[0])+"yyyyyttttt", "")
                                        rep = rep.replace("yyyyyttttt", "&&&&&&&&&&&&&&&&&&&&")
                                        rep = rep.replace("//admin/k", "/AdminK")
                                        rep = rep.replace("//admin/e", "/AdminE")
                                        rep = rep.replace("//admin/D", "/AdminD")
                                        rep = rep.replace("//admin/I", "/AdminI")
                                        repo = rep.replace("//admin/C", "/AdminC")
                                        sock.send(repo.encode())
                                        print("ENVOYER" + rep)
                            except Exception as e:
                                print(e)
                    except Exception as e:
                        del clients[conn]
                        print("%s has left the chat." % data)
                        print(e)

                        break

                except Exception as e:
                    del clients[conn]
                    print("%s has left the chat." % data)
                    print(e)
                    break




            # Recevoir le nom du fichier
            # nom_fichier = conn.recv(1024).decode()
            # taille = conn.recv(1024).decode()
            # taille = int(taille)
            # i = 0
            # # Créer un dossier de destination s'il n'existe pas
            # if not os.path.exists('fichiers_recus'):
            #     os.makedirs('fichiers_recus')
            #
            # # Enregistrer le fichier
            # with open(os.path.join('/home/justin/Vidéos/fichier', nom_fichier), 'wb') as fichier:
            #     while True:
            #
            #         # Recevoir des données par blocs
            #         data = conn.recv(1073741824)
            #
            #         # Fin de la transmission
            #         try:
            #             print(data.decode())
            #         except:
            #             A = 1
            #         try:
            #             if len(data) < 1:
            #                 print('fin')
            #
            #                 break
            #         except Exception as e:
            #             a = 1
            #
            #         # Ecrire les données dans le fichier
            #         fichier.write(data)
            #         conn.sendall(data)
            #         i = i + len(data)
            #         if i >= taille:
            #             print('fin')
            #             break
            #         print(i)
            #         print(taille)

            # Envoyer un message de confirmation
            print('Fichier reçu avec succès !')



    except:
        del clients[conn]
        print("%s has left the chat." % data)


def broadcast(msg, prefix=""):
    for sock in clients:
        sock.send(bytes(prefix, "utf8") + msg)


def datasend(dat, destinateur):
    for sock in clients:
        if clients[conn] in destinateur:
            print(clients[conn])
            conn.sendall(dat)


while True:
    conn, addr = s.accept()
    if (addr==""):
        a=1
    else:

        print("%s:%s has connected." % addr)
        conn.send("Bienvenue".encode())
        addresses[conn] = addr
        threading.Thread(target=handle_client, args=(conn,)).start()
