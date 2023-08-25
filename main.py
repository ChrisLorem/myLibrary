#ligne  471 affichage de nom user

import string
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
import customtkinter as ctk
from pathlib import Path
import sqlite3
import datetime
from datetime import date
from PIL import ImageTk, Image
import qrcode
import random

date = datetime.datetime.now()


class Livre():
    def __init__(self,id,titre,auteur,annee,nombre,stock,genre,langue,emplacement,date):
        self.id = id
        self.titre = titre
        self.auteur = auteur
        self.annee = annee
        self.nombre = nombre
        self.stock = stock
        self.genre = genre
        self.langue = langue
        self.emplacement = emplacement
        self.date = date

class User():
    def __init__(self,id,Nom,prenom,age,debut,qr,numero,adresse,expiration,categorie):
        self.id = id
        self.nom = Nom
        self.prenom = prenom
        self.age = age
        self.debut = debut
        self.qr = qr
        self.numero = numero
        self.adresse = adresse
        self.expiration = expiration
        self.categorie = categorie

class Bibliotheque():
    def __init__(self):
        self.db_connection = sqlite3.connect("biblio.db")
        self.cursor = self.db_connection.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS b_tables(id INT,titre TEXT,auteur TEXT,annee INT,nombre INT,stock INT,genre INT,langue INT,emplacement INT,date INT)")
        self.db_connection.commit()
    
    def ajouter_livre(self,livre):
        self.cursor.execute("INSERT INTO b_tables (id,titre,auteur,annee,nombre,stock,genre,langue,emplacement,date) VALUES (?,?,?,?,?,?,?,?,?,?)",(livre.id,livre.titre,livre.auteur,livre.annee,livre.nombre,livre.stock,livre.genre,livre.langue,livre.emplacement,livre.date))
        self.db_connection.commit()
        print("le livre à été bien enregistré..")

    def supprimer_livre(self,id):
        self.db_connection.commit()
        self.cursor.execute("DELETE FROM b_tables WHERE id=?",(id,))
        self.db_connection.commit()
        print("le livre à été bien supprimé")
    
    def afficher_livre_id(self,id):
        result = self.cursor.execute("SELECT * FROM b_tables WHERE id=?",(id,))
        for element in result:
            print(element)
            id,titre,auteur,annee,nombre,stock,genre,langue,emplacement,date = (element[0]),(element[1]),(element[2]),(element[3]),(element[4]),(element[5]),(element[6]),(element[7]),(element[8]),(element[9])
        return id,titre,auteur,annee,nombre,stock,genre,langue,emplacement,date

    def afficher_livre_titre(self,titre):
        result = self.cursor.execute("SELECT * FROM b_tables WHERE id=?",(titre,))
        for element in result:
            id,titre,auteur,annee,nombre,stock,genre,langue,emplacement,date = (element[0]),(element[1]),(element[2]),(element[3]),(element[4]),(element[5]),(element[6]),(element[7]),(element[9])
        return id,titre,auteur,annee,nombre,stock,genre,langue,emplacement,date
            
    def afficher_tout(self):
        self.db_connection.commit()
        self.cursor.execute("SELECT * FROM b_tables")
        result = self.cursor.fetchall()
        for element in result:
            id,titre,auteur,annee,nombre,stock,genre,langue,emplacement,date = (element[0]),(element[1]),(element[2]),(element[3]),(element[4]),(element[5]),(element[6]),(element[7]),(element[9])
        return id,titre,auteur,annee,nombre,stock,genre,langue,emplacement,date

    
class Admin():
    def __init__(self):
        self.db_connection = sqlite3.connect("biblio.db")
        self.cursor = self.db_connection.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS u_tables(id INT,nom TEXT,prenom TEXT,age INT,debut INT,qr INT,numero TEXT,adresse TEXT,expiration TEXT,categorie TEXT)")
        self.db_connection.commit()
    
    def ajouter_user(self,user):
        self.cursor.execute("INSERT INTO u_tables (id,nom,prenom,age,debut,qr,numero,adresse,expiration,categorie) VALUES (?,?,?,?,?,?,?,?,?,?)",(user.id,user.nom,user.prenom,user.age,user.debut,user.qr,user.numero,user.adresse,user.expiration,user.categorie))
        self.db_connection.commit()
        print("l'user à été bien enregistré..")

    def supprimer_user(self,id):
        self.cursor.execute("DELETE FROM u_tables WHERE id=?",(id,))
        self.db_connection.commit()
        print("le user à été bien supprimé")
    
    def afficher_user_id(self,id):
        result = self.cursor.execute("SELECT * FROM u_tables WHERE id=?",(id,))
        for element in result:
            id,nom,prenom,age,debut,qr,numero,adresse,expiration,categorie = (element[0]),(element[1]),(element[2]),(element[3]),(element[4]),(element[5]),(element[6]),(element[7]),(element[8]),(element[9])
        return id,nom,prenom,age,debut,qr,numero,adresse,expiration,categorie

    def afficher_user_nom(self,prenom):
        result = self.cursor.execute("SELECT * FROM u_tables WHERE id=?",(prenom,))
        for element in result:
            id,nom,prenom,age,debut,qr,numero,adresse,expiration,categorie = (element[0]),(element[1]),(element[2]),(element[3]),(element[4]),(element[5]),(element[6]),(element[7]),(element[8]),(element[9])
        return id,nom,prenom,age,debut,qr,numero,adresse,expiration,categorie
            
    def afficher_tout(self):
        self.db_connection.commit()
        self.cursor.execute("SELECT * FROM u_tables")
        result = self.cursor.fetchall()
        for element in result:
            id,nom,prenom,age,debut,qr,numero,adresse,expiration,categorie = (element[0]),(element[1]),(element[2]),(element[3]),(element[4]),(element[5]),(element[6]),(element[7]),(element[8]),(element[9])
        return id,nom,prenom,age,debut,qr,numero,adresse,expiration,categorie


def show_date():
    day = datetime.datetime.now().day
    month = datetime.datetime.now().month
    year = datetime.datetime.now().year
    date = (str(day) + ":" + str(month) + ":" + str(year))
    return date

def front():
    ASSETS_PATH = Path(__file__).resolve().parent / "assets"
    window = tk.Tk()

    logo = tk.PhotoImage(file=ASSETS_PATH / "iconbitmap.gif")
    window.call('wm', 'iconphoto', window._w, logo)
    window.title("Lorem Lorem")

    def get_maxscreen_size(window):
        global screen_height,screen_width
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        print(screen_width,screen_height)
        window.geometry(f"{screen_width}x{screen_height}")


    get_maxscreen_size(window)


    canvas = tk.Canvas(
        window, bg="#cacaca", width=screen_width,height=screen_height)
    canvas.place(x=0, y=0)

    canvas.create_rectangle(160, 0, 1319,70, fill="#00a6d8",outline="#00a6d8",tags="Lorem's lib")
    logo_front = tk.PhotoImage(file=ASSETS_PATH / "book.png")
    canvas.create_image(595, 40, image=logo_front)

    canvas.create_rectangle(0, 0, 160,70, fill="#cacaca",outline="#bebebe",tags="admin")
    admin_front = tk.PhotoImage(file=ASSETS_PATH /"person.png").subsample(2,2)
    canvas.create_image(35,30, image=admin_front)

    canvas.create_rectangle(0, 70, 160,700, fill="#00a6d8",outline="#00a6d8",tags="menu")
    
    # canvas.create_rectangle(160, 70, 1319,700, fill="#fafafa",outline="#fafafa",tags="main")

    canvas.create_rectangle(160, 70, 1319,100, fill="#cacaca",outline="#bebebe",tags="titre")

    canvas.create_text(
        720,85,text="Accueil",fill="#000",font=("Courier New",13,"bold"),tags="home_label"
    )
    canvas.create_text(
        720,40,text="Lorem's Library",fill="#000",font=("Arial-BoldMT",16,"bold")
    )
    canvas.create_text(
        80,37,text="Admin",fill="#000",font=("Arial-BoldMT",13,"bold")
    )

    canvas1 = tk.Canvas(
        canvas, bg="#fff",width=screen_width-160,height=screen_height-100)
    canvas1.place(x=160, y=100)

    image_path = ASSETS_PATH / "fond1.jpg"
    img = Image.open(image_path)
    bg = ImageTk.PhotoImage(img)
    background_label = tk.Label(canvas1, image=bg)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    


    def remove():
        clear_canvas(canvas1)
        element = canvas.find_enclosed(160, 70, 1319,600)
        for widget in element:
            canvas.delete(widget)
        canvas1.delete("rectangle")


    def clear_canvas(canvas):
        for widget in canvas.winfo_children():
             widget.destroy()

    def menu():
        def home_book():
            remove()
            canvas.create_text(
                720,85,text="Accueil",fill="#000",font=("Courier New",13,"bold"),tags="home_label"
            )
            home_main()
            home_menu.config(relief=tk.SUNKEN)
            add_menu.config(relief=tk.RAISED)
            update_menu.config(relief=tk.RAISED)
            home_user.config(relief=RAISED)
            add_user.config(relief=RAISED)
            update_user.config(relief=RAISED)
            borrow_menu.config(relief=RAISED)

        def adding_book():
            remove()
            canvas.create_text(
                720,85,text="Ajout des livres",fill="#000",font=("Courier New",13,"bold"),tags="add_label"
            )
            adding_main()
            home_menu.config(relief=tk.RAISED)
            add_menu.config(relief=tk.SUNKEN)
            update_menu.config(relief=tk.RAISED)
            home_user.config(relief=RAISED)
            add_user.config(relief=RAISED)
            update_user.config(relief=RAISED)
            borrow_menu.config(relief=RAISED)


        def update_book():
            remove()
            canvas.create_text(
                720,85,text="Modification",fill="#000",font=("Courier New",13,"bold"),tags="update_label"
            )
            update_main()
            home_menu.config(relief=tk.RAISED)
            add_menu.config(relief=tk.RAISED)
            update_menu.config(relief=tk.SUNKEN)
            home_user.config(relief=RAISED) 
            add_user.config(relief=RAISED)
            update_user.config(relief=RAISED)
            borrow_menu.config(relief=RAISED)
        
        def borrow_book():
            remove()
            canvas.create_text(
                720,85,text="gestion des emprunts et de retour des liivres",fill="#000",font=("Courier New",13,"bold"),tags="update_label"
            )
            home_user.config(relief=RAISED)
            add_user.config(relief=RAISED)
            update_user.config(relief=RAISED)
            home_menu.config(relief=tk.RAISED)
            add_menu.config(relief=tk.RAISED)
            update_menu.config(relief=tk.RAISED)
            borrow_menu.config(relief=SUNKEN)
            borrows()

        def home_use():
            remove()
            canvas.create_text(
                720,85,text="Membres",fill="#000",font=("Courier New",13,"bold"),tags="update_label"
            )
            home_user_main()
            home_user.config(relief=SUNKEN)
            add_user.config(relief=RAISED)
            update_user.config(relief=RAISED)
            home_menu.config(relief=tk.RAISED)
            add_menu.config(relief=tk.RAISED)
            update_menu.config(relief=tk.RAISED)
            borrow_menu.config(relief=RAISED)
            


        def add_use():
            remove()
            canvas.create_text(
                720,85,text="Ajout des membres",fill="#000",font=("Courier New",13,"bold"),tags="update_label"
            )
            adding_main_user()
            home_user.config(relief=RAISED)
            add_user.config(relief=SUNKEN)
            update_user.config(relief=RAISED)
            home_menu.config(relief=tk.RAISED)
            add_menu.config(relief=tk.RAISED)
            update_menu.config(relief=tk.RAISED)
            borrow_menu.config(relief=RAISED)


        def update_use():
            remove()
            canvas.create_text(
                720,85,text="Statut et modification des membres",fill="#000",font=("Courier New",13,"bold"),tags="update_label"
            )
            home_user.config(relief=RAISED)
            add_user.config(relief=RAISED)
            update_user.config(relief=SUNKEN)
            home_menu.config(relief=tk.RAISED)
            add_menu.config(relief=tk.RAISED)
            update_menu.config(relief=tk.RAISED)
            borrow_menu.config(relief=RAISED)
            update_main_user()

    
        def desconnect():
            if messagebox.askokcancel("Déconnexion","Voulez-vous vraiment déconnecter"):
                window.destroy()


        home_menu = tk.Button(canvas,text="livres",width=14,command=home_book)
        home_menu.place(x=5,y=74)

        add_menu = tk.Button(canvas,text="Ajouter livres",width=14,command=adding_book)
        add_menu.place(x=5,y=109) 

        update_menu = tk.Button(canvas,text="Modifier livres",width=14,command=update_book)
        update_menu.place(x=5,y=144)

        borrow_menu = tk.Button(canvas,text="Emprunt des livres",width=14,command=borrow_book)
        borrow_menu.place(x=5,y=179)

        home_user = tk.Button(canvas,text="membre",width=14,command=home_use)
        home_user.place(x=5,y=300)

        add_user = tk.Button(canvas,text="ajouter membre",width=14,command=add_use)
        add_user.place(x=5,y=335)

        update_user = tk.Button(canvas,text="modifier membre",width=14,command=update_use)
        update_user.place(x=5,y=370)


        disconnect_admin = ctk.CTkButton(canvas,text="Déconnexion",width=40,command=desconnect,border_color="")
        disconnect_admin.place(x=20,y=440)
            
        
        def borrows():
            global Titre_livre_empentry

            def smartsearch_emprunt(event):
                global height_list
                search_term = Titre_livre_empentry.get()
                conn = sqlite3.connect("biblio.db")
                cursor = conn.cursor()
                cursor.execute("SELECT titre FROM b_tables WHERE titre LIKE ?", ('%' + search_term + '%',))
                results = cursor.fetchall()
                height_list = len(results)
                listbox_emp.delete(0, tk.END)
                for title in results:
                    listbox_emp.insert(tk.END, title[0])    
                listbox_emp.config(height=height_list)
                
            def smartsearch_rendu(event):
                global height_list
                search_term = Titre_livre_empentry.get()
                conn = sqlite3.connect("biblio.db")
                cursor = conn.cursor()
                cursor.execute("SELECT titre FROM b_tables WHERE titre LIKE ?", ('%' + search_term + '%',))
                results = cursor.fetchall()
                height_list = len(results)
                listbox_rendu.delete(0, tk.END)
                for title in results:
                    listbox_rendu.insert(tk.END, title[0])
                listbox_rendu.config(height=height_list)


            def listener_select_emprunt(event):
                selected_index = listbox_emp.curselection()
                if selected_index:
                    selected_title = listbox_emp.get(selected_index)
                    Titre_livre_empentry.delete(0, tk.END)
                    Titre_livre_empentry.insert(0, selected_title)
                    listbox_emp.destroy()

            def listener_select_rendu(event):
                selected_index = listbox_rendu.curselection()
                if selected_index:
                    selected_title = listbox_rendu.get(selected_index)
                    Titre_livre_rendentry.delete(0, tk.END)
                    Titre_livre_rendentry.insert(0, selected_title)
                    listbox_rendu.destroy()
            
            def about_book_emp():
                try:
                    conn = sqlite3.connect("biblio.db")
                    cursor = conn.cursor()
                    result = cursor.execute("SELECT stock FROM b_tables WHERE titre=?",(Titre_livre_empentry.get(),))
                    result = result.fetchone()[0]
                    new_stock = result - 1
                    query = f"UPDATE b_tables SET stock=? WHERE titre=?"
                    cursor.execute(query,(new_stock,Titre_livre_empentry.get()))
                    conn.commit()


                    Nom_borrows = cursor.execute("SELECT * FROM u_tables WHERE id=?",(Id_membre_empentry.get(),))
                    Nom_borrows = Nom_borrows.fetchall()[0] 
                    conn.close()
                    Nom_emprunt = Nom_borrows[1] +" "+Nom_borrows[2]
                    

                    Title = ctk.CTkLabel(canvas1,text=f"Titre :  {Titre_livre_empentry.get()}",text_color="black",font=font1)
                    Title.place(x=60,y=300)

                    Label_emp = ctk.CTkLabel(canvas1,text=f"Nom de l'emprunteur :  {Nom_emprunt}",text_color="black",font=font1)
                    Label_emp.place(x=60,y=330)


                    Reste = ctk.CTkLabel(canvas1,text=f"Exemplaire en stock :  {new_stock} restants",text_color="black",font=font1)
                    Reste.place(x=60,y=360)


                    mois = ["janvier","fevrier","mars","avril","mai","juin","juillet","août","septembre","octobre","novembre","decembre"]
                    new_month = date.month + 1
                    mois_de_retour = (mois[new_month])
                    retour = (str(date.day) +" "+ mois_de_retour +" "+str(date.year))
                    date_retour = ctk.CTkLabel(canvas1,text=f"Retourné le :  {retour}",text_color="black",font=font1)
                    date_retour.place(x=60,y=390)
                except:
                    messagebox.showerror("Erreur d'affichage","Veuillez verifiez que tous les entrées soient rempli")

                
            def about_book_return():
                try:
                    conn = sqlite3.connect("biblio.db")
                    cursor = conn.cursor()
                    result = cursor.execute("SELECT stock FROM b_tables WHERE titre=?",(Titre_livre_rendentry.get(),))
                    result = result.fetchone()[0]
                    new_stock = result + 1
                    query = f"UPDATE b_tables SET stock=? WHERE titre=?"
                    cursor.execute(query,(new_stock,Titre_livre_rendentry.get()))
                    conn.commit()


                    Nom_borrows = cursor.execute("SELECT * FROM u_tables WHERE id=?",(Id_membre_rendentry.get(),))
                    Nom_borrows = Nom_borrows.fetchall()[0] 
                    conn.close()
                    Nom_emprunt = Nom_borrows[1] +" "+Nom_borrows[2]
                    

                    Title = ctk.CTkLabel(canvas1,text=f"Titre :  {Titre_livre_rendentry.get()}",text_color="black",font=font1)
                    Title.place(x=640,y=300)

                    Label_emp = ctk.CTkLabel(canvas1,text=f"Nom de l'emprunteur :  {Nom_emprunt}",text_color="black",font=font1)
                    Label_emp.place(x=640,y=330)


                    Reste = ctk.CTkLabel(canvas1,text=f"Exemplaire en stock :  {new_stock} restants",text_color="black",font=font1)
                    Reste.place(x=640,y=360)


                    mois = ["janvier","fevrier","mars","avril","mai","juin","juillet","août","septembre","octobre","novembre","decembre"]
                    month_return = date.month
                    mois_de_retour = (mois[month_return])
                    retour = (str(date.day) +" "+ mois_de_retour +" "+str(date.year))
                    date_retour = ctk.CTkLabel(canvas1,text=f"Retourné le :  {retour}",text_color="black",font=font1)
                    date_retour.place(x=640,y=390)
                except:
                    messagebox.showerror("Erreur d'affichage","Veuillez verifiez que tous les entrées soient rempli")



            emprunt_titre = tk.Label(canvas1,width="30",text="EMPRUNT",fg="black",font=("Arial-Black",20))
            emprunt_titre.place(x=20,y=20)

            Id_membre_emplabel = tk.Label(canvas1,text="ID du membre :",fg="black",font=("Arial-Black",11),bg="#fff")
            Id_membre_emplabel.place(x=60,y=100)

            Id_membre_empentry = ctk.CTkEntry(canvas1,width=100,height=11,border_color="#00a6d8",fg_color="#fff",text_color="black")
            Id_membre_empentry.place(x=220,y=100)

            Titre_livre_emplabel = tk.Label(canvas1,text="Titre du livre   :",fg="black",font=("Arial-Black",11),bg="#fff")
            Titre_livre_emplabel.place(x=60,y=140)

            Titre_livre_empentry = tk.Entry(canvas1,width=24)
            Titre_livre_empentry.place(x=220,y=140)
            Titre_livre_empentry.bind("<KeyRelease>", smartsearch_emprunt)

            listbox_emp = tk.Listbox(canvas1, width=24,height=0,highlightbackground="#fff",background="white")
            listbox_emp.place(x=220,y=162)
            listbox_emp.bind("<<ListboxSelect>>", listener_select_emprunt)

            approved_button_emp = tk.Button(canvas1, width=7,text="emprunter",command=about_book_emp)
            approved_button_emp.place(x=440,y=140)

            font1 = ctk.CTkFont(size=14)


            #Rendu du livre
            rendu_titre = tk.Label(canvas1,width="30",text="RENDU",fg="black",font=("Arial-Black",20))
            rendu_titre.place(x=600,y=20)

            Id_membre_rendlabel = tk.Label(canvas1,text="ID du membre :",fg="black",font=("Arial-Black",11),bg="#fff")
            Id_membre_rendlabel.place(x=640,y=100)

            Id_membre_rendentry = ctk.CTkEntry(canvas1,width=100,height=11,border_color="#00a6d8",fg_color="#fff",text_color="black")
            Id_membre_rendentry.place(x=800,y=100)

            Titre_livre_rendlabel = tk.Label(canvas1,text="Titre du livre   :",fg="black",font=("Arial-Black",11),bg="#fff")
            Titre_livre_rendlabel.place(x=640,y=140)

            Titre_livre_rendentry = tk.Entry(canvas1,width=24)
            Titre_livre_rendentry.place(x=800,y=140)
            Titre_livre_rendentry.bind("<KeyRelease>", smartsearch_rendu)

            listbox_rendu = tk.Listbox(canvas1, width=24,height=0,highlightbackground="#fff",background="white")
            listbox_rendu.place(x=800,y=162)
            listbox_rendu.bind("<<ListboxSelect>>", listener_select_rendu)

            approved_button_rend = tk.Button(canvas1, width=7,text="rendre",command=about_book_return)
            approved_button_rend.place(x=1020,y=140)


        def home_user_main():
            global search,l1,searching,show_all_button,recherche_entry,recherche_button,recherche_label,table
            
            search = tk.Frame(canvas1,width=1143,height=65)
            search.place(x=10,y=10)

            l1 = tk.Label(canvas1,text="Chercher un utilisiteur",fg="black",font=("Arial",11,"bold"))
            l1.place(x=40,y=10)

            values = ["ID","nom","prenom","age","debut","qr","expiration","categorie"]
            


            recherche_label = ttk.Combobox(canvas1,values=values)
            recherche_label.bind("<<ComboboxSelected>>",selected_options_user)
            recherche_label.set("Afficher par")
            recherche_label.place(x=50,y=37)

            recherche_entry = tk.Entry(canvas1)
            recherche_entry.place(x=250,y=36)
            recherche_button = tk.Button(canvas1,text="rechercher",width=7,command=rechercher_user)
            recherche_button.place(x=440,y=30)
            show_all_button = tk.Button(canvas1,text="Afficher tout",width=8,command=vraiment_afficher_tout_user)
            show_all_button.place(x=540,y=30)

            search_icon = tk.PhotoImage(file=ASSETS_PATH / "search24.png")
            searching = tk.Label(canvas1,image=search_icon)
            searching.image = search_icon
            searching.place(x=10,y=10)

            table = ttk.Treeview(canvas1,columns=("col1","col2","col3","col4","col5","col6","col7","col8","col9","col10"),show="headings")
            table.configure(height=24)
            table.heading("col1",text="ID")
            table.heading("col2", text="nom")
            table.heading("col3", text="prenom")
            table.heading("col4", text="age")
            table.heading("col5", text="debut")
            table.heading("col6", text="qr")
            table.heading("col7", text="numero")
            table.heading("col8", text="adresse")
            table.heading("col9", text="expiration")
            table.heading("col10", text="categorie")

            

            table.column("col1",width=50,anchor="center")
            table.column("col2",width=140,anchor="center")
            table.column("col3",width=90,anchor="center")
            table.column("col4",width=50,anchor="center")
            table.column("col5",width=100,anchor="center")
            table.column("col6",width=100,anchor="center")
            table.column("col7",width=140,anchor="center")
            table.column("col8",width=220,anchor="center")
            table.column("col9",width=100,anchor="center")
            table.column("col10",width=150,anchor="center")



            table.configure(style="Custom.Treeview")

            style = ttk.Style()
            style.configure("Custom.Treeview", highlightthickness=0, bd=0, font=("Helvetica", 10))
            style.configure("Custom.Treeview.Heading", font=("Helvetica", 13, "bold"))
            table.place(x=10,y=85)

        def selected_options_user(event):
            options_user = recherche_label.get()
            return options_user


        def vraiment_afficher_tout_user():
            conn = sqlite3.connect("biblio.db")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM u_tables")
            rows = cursor.fetchall()
            table.delete(*table.get_children())
            for row in rows:
                id,nom,prenom,age,debut,qr,numero,adresse,expiration,categorie = (row[0]),(row[1]),(row[2]),(row[3]),(row[4]),(row[5]),(row[6]),(row[7]),(row[8]),(row[9])
                table.insert("", "end", values=(id, nom, prenom,age,debut,qr,numero,adresse,expiration,categorie))
            conn.close()

        def rechercher_user():
            table.delete(*table.get_children())
            def verify_options():
                global options
                options = selected_options_user(None)
                different_options = ["ID","nom","prenom","age","debut","qr"]
                if options in different_options:
                    print(options)
                else:
                    options = "ID"    
                return options
            options_user = verify_options()
            
                
            titre_recherche_user = recherche_entry.get()
            conn = sqlite3.connect("biblio.db")
            cursor = conn.cursor()
            result = cursor.execute(f"SELECT * FROM u_tables WHERE prenom LIKE ? ORDER BY {options_user}",('%' + titre_recherche_user + '%',))
            row1 = result.fetchall()
            print(row1)
            conn.close()
            if row1 is not None:
                for row in row1:
                    id,nom,prenom,age,debut,qr,numero,adresse,expiration,categorie = (row[0]),(row[1]),(row[2]),(row[3]),(row[4]),(row[5]),(row[6]),(row[7]),(row[8]),(row[9])
                    table.insert("","end", values=(id,nom,prenom,age,debut,qr,numero,adresse,expiration,categorie))
            else:
                table.destroy()
                error_label = tk.Label(canvas, text="Aucune correspondance",font=("Helvetica",13),fg="red",bg="#fff")        
                error_label.place(x=175,y=190)
                print("Aucune résultat trouvé")

        def adding_main_user():
            global search,nom,nom_entry,auteur,auteur_entry,annee,annee_combobox
            search = tk.Frame(canvas1,width=1143,height=550)
            search.place(x=10,y=10)

            nom = tk.Label(search,text="Nom du membre :     ")
            nom.place(x=20,y=60)
            nom_entry = ctk.CTkEntry(search,width=170,height=35,border_color="#00a6d8",fg_color="#fff",text_color="black")
            nom_entry.place(x=400,y=55)

            prenom = tk.Label(search,text="Prenom du membre         ")
            prenom.place(x=20,y=110)
            prenom_entry = ctk.CTkEntry(search,width=170,height=35,border_color="#00a6d8",fg_color="#fff",text_color="black")   
            prenom_entry.place(x=400,y=105)

            age = tk.Label(search,text="Age du membre           ")
            age.place(x=20,y=160)
            
            age_val = []
            for i in range(3,100):
                age_val.append(str(i))


            age_combobox = ctk.CTkComboBox(master=search,width=80,border_color="#00a6d8",fg_color="#fff",text_color="black",values=age_val,dropdown_fg_color="white",dropdown_text_color="black",dropdown_hover_color="#00a6d8",button_color="#00a6d8")
            age_combobox.place(x=400,y=155)

            numero = tk.Label(search,text="Numéro de téléphone         ")
            numero.place(x=20,y=215)
            numero_entry = ctk.CTkEntry(search,width=170,height=35,border_color="#00a6d8",fg_color="#fff",text_color="black")
            numero_entry.place(x=400,y=205)

            adresse = tk.Label(search,text="Adresse du membre         ")
            adresse.place(x=20,y=260)
            adresse_entry = ctk.CTkEntry(search,width=170,height=35,border_color="#00a6d8",fg_color="#fff",text_color="black")
            adresse_entry.place(x=400,y=255)

            expiration = tk.Label(search,text="Expiration de l'abonnement           ")
            expiration.place(x=20,y=315)

            # exp_tab = []
            # for i in range(1,6):
            #     exp_tab.append(str(i)+"ans")
            exp_tab = ["1 an","2 ans","3 ans","4 ans"]

            expiration_entry = ctk.CTkComboBox(search,width=170,height=35,values=exp_tab,border_color="#00a6d8",fg_color="#fff",text_color="black",button_color="#00a6d8",dropdown_hover_color="#00a6d8")
            expiration_entry.place(x=400,y=305)

            categorie_list = ["gratuite","payante","etudiants","enfants","visiteurs"]

            categorie = tk.Label(search,text="Catégorie du membre           ")
            categorie.place(x=20,y=365)
            categorie_combobox = ctk.CTkComboBox(master=search,width=170,height=35,border_color="#00a6d8",fg_color="#fff",text_color="black",values=categorie_list,dropdown_fg_color="white",dropdown_text_color="black",dropdown_hover_color="#00a6d8",button_color="#00a6d8")
            categorie_combobox.place(x=400,y=355)

            day = datetime.datetime.now().day
            month = datetime.datetime.now().month
            year = datetime.datetime.now().year
            date = (str(day) + "/" + str(month) + "/" + str(year))
            var = StringVar()
            var.set(date)

            def get_id_user():
                conn = sqlite3.connect("biblio.db")
                conn.commit()
                cursor = conn.cursor()
                try:
                    cursor.execute("SELECT id FROM u_tables ORDER BY id DESC LIMIT 1")
                    row = cursor.fetchone()
                    if row is not None:
                        last_id = row[0]
                    conn.close()
                    return last_id
                except:
                    last_id = 0
                    return last_id
                
            
            def generate_random_alphanumeric():
                alphanumeric_chars = string.ascii_letters + string.digits
                random_alphanumeric = ''.join(random.choice(alphanumeric_chars) for _ in range(5))
                return random_alphanumeric

            def create_qr():
                qr = generate_random_alphanumeric()
                return qr
            
            def display_qr_code(qr):
                qr_image = qrcode.make(qr)
                qr_image = qr_image.resize((80, 80), Image.ANTIALIAS)
                img = ImageTk.PhotoImage(qr_image)
                qr_label = tk.Label(canvas1)
                qr_label.place(x=630,y=310)
                qr_label.config(image=img)
                qr_label.image = img
                return qr_label

            def ajout_users():
                last_id = get_id_user()
                new_id = last_id + 1
                nom_user = nom_entry.get()
                prenom_user = prenom_entry.get()
                age_user = age_combobox.get()
                debut_user = show_date()
                qr_user = create_qr()
                numero_user = numero_entry.get()
                adresse_user = adresse_entry.get()
                expiration_user = expiration_entry.get()
                categorie_user = categorie_combobox.get()

                if new_id and nom_user and prenom_user  and age_user and debut_user and  qr_user and numero_user and adresse_user and expiration_user and categorie_user:
                    Admin1 = Admin()
                    User1 = User(new_id, nom_user, prenom_user, age_user, debut_user, qr_user, numero_user, adresse_user, expiration_user, categorie_user)
                    Admin1.ajouter_user(User1)
                    remove()



                    id_user,nom_user,prenom_user,age_user,qr_user,expiration_user,categorie_user =new_id ,nom_user,prenom_user,age_user,qr_user,expiration_user,categorie_user

                    canvas1.create_rectangle(260, 100, 720,400,outline="#444444",width=2,tags="rectangle")

                    Titre = ctk.CTkLabel(canvas1,text=f"CARTE DU MEMBRE N°{id_user} ",text_color="black",font=("",20,"bold"))
                    Titre.place(x=400,y=10)

                    print_card = ctk.CTkButton(canvas1,text="Imprimer la carte",font=("Arial-Black",18))
                    print_card.place(x=400,y=450)

                    
                    jhon_doe = tk.PhotoImage(file=ASSETS_PATH / "jd.png").subsample(5)
                    show_doe = tk.Label(canvas1,image=jhon_doe)
                    show_doe.image = jhon_doe
                    show_doe.place(x=263,y=103)

                    display_qr_code(qr_user)

                    social_media = ctk.CTkLabel(canvas1,text="Lorem's Library",text_color="black",font=("",13,"bold"))
                    social_media.place(x=510,y=370)


                    fb_icon = tk.PhotoImage(file=ASSETS_PATH / "facebook.png").subsample(18)
                    show_font = tk.Label(canvas1,image=fb_icon)
                    show_font.image = fb_icon
                    show_font.place (x=470,y=365)



                    Nom_label = ctk.CTkLabel(canvas1,text="Nom : ",text_color="black",font=("",14,"bold"))
                    Nom_label.place(x=280,y=220)

                    Nom_value = ctk.CTkLabel(canvas1,text=nom_user,text_color="black",font=("",13))
                    Nom_value.place(x=350,y=220)

                    # create_horizontal_line(canvas1,150,250,300)

                    Prenom_label = ctk.CTkLabel(canvas1,text="Prénom : ",text_color="black",font=("",14,"bold"))
                    Prenom_label.place(x=280,y=250)

                    Prenom_value = ctk.CTkLabel(canvas1,text=prenom_user,text_color="black",font=("",13))
                    Prenom_value.place(x=380,y=250)

                    age_label = ctk.CTkLabel(canvas1,text="Age : ",text_color="black",font=("",14,"bold"))
                    age_label.place(x=280,y=280)

                    age_value = ctk.CTkLabel(canvas1,text=age_user+" ans",text_color="black",font=("",13))
                    age_value.place(x=350,y=280)

                    categorie_label = ctk.CTkLabel(canvas1,text="Catégorie : ",text_color="black",font=("",14,"bold"))
                    categorie_label.place(x=280,y=310)

                    categorie_value = ctk.CTkLabel(canvas1,text=categorie_user,text_color="black",font=("",13))
                    categorie_value.place(x=390,y=310)

                    phone_icon = tk.PhotoImage(file=ASSETS_PATH / "phone.png").subsample(18)
                    show_font = tk.Label(canvas1,image=phone_icon,background="#fff")
                    show_font.image = phone_icon
                    show_font.place (x=265,y=365)

                    contact_biblio = ctk.CTkLabel(canvas1,text="+261 020 24 607 41",text_color="black",font=("",13,"bold"))
                    contact_biblio.place(x=300,y=370)

                    Label_lib = ctk.CTkLabel(canvas1,text="LOREM'S LIBRARY",text_color="#2bc3ce",font=("Roboto",21,"bold"))
                    Label_lib.place(x=470,y=120)

                    logo_lorem = tk.PhotoImage(file=ASSETS_PATH / "iconbitmap.gif").subsample(4)
                    show_logo = tk.Label(canvas1,image=logo_lorem,background="#fff")
                    show_logo.image = logo_lorem
                    show_logo.place (x=390,y=103)
                else:
                    messagebox.showerror("Champs incomplet","veuillez vérifiéz que tous les champs soient remplissent")

                

            submit = ctk.CTkButton(master=search,fg_color=("white","#00a6d8"),text="Enregistrer",command=ajout_users)
            submit.place(x=100,y=400)

            



        def update_main_user():
            global recherche_option,recherche_entry,table,tab1,search,recherche_button,recherche_label
            search = tk.Frame(canvas1,width=1143,height=70)
            search.place(x=10,y=10)

            # tab1 = tk.Frame(canvas1,width=1319,height=500)
            # tab1.place(x=10,y=90)


            l1 = tk.Label(search,text="Chercher une membre par son ID",fg="black",font=("Arial",11,"bold"))
            l1.place(x=30,y=4)
            search_icon = tk.PhotoImage(file=ASSETS_PATH / "search24.png")
            searching = tk.Label(search,image=search_icon)
            searching.image = search_icon
            searching.place(x=0,y=4)

            values = ["ID"]

            recherche_option  = ttk.Combobox(search,text="Chercher par:",values=values)
            recherche_option.bind("<<ComboboxSelected>>",selected_options2_user)
            recherche_option.set("Rechercher par")
            recherche_option.place(x=50,y=30)

            recherche_entry = tk.Entry(search)
            recherche_entry.place(x=240,y=29)
            recherche_button = tk.Button(search,text="rechercher",width=7,command=rechercher_par_ID_user)
            recherche_button.place(x=450,y=27)


            table = ttk.Treeview(canvas1,columns=("col1","col2","col3","col4","col5","col6","col7","col8","col9","col10"),show="headings")
            table.configure(height=1)
            table.heading("col1",text="ID")
            table.heading("col2", text="nom")
            table.heading("col3", text="prenom")
            table.heading("col4", text="Age")
            table.heading("col5", text="Début")
            table.heading("col6", text="QR")
            table.heading("col7", text="numero")
            table.heading("col8", text="adresse")
            table.heading("col9", text="expiration")
            table.heading("col10", text="categorie")

            table.column("col1",width=50,anchor="center")
            table.column("col2",width=140,anchor="center")
            table.column("col3",width=90,anchor="center")
            table.column("col4",width=50,anchor="center")
            table.column("col5",width=100,anchor="center")
            table.column("col6",width=100,anchor="center")
            table.column("col7",width=140,anchor="center")
            table.column("col8",width=220,anchor="center")
            table.column("col9",width=100,anchor="center")
            table.column("col10",width=200,anchor="center")
            



            table.configure(style="Custom.Treeview")

            style = ttk.Style()
            style.configure("Custom.Treeview", highlightthickness=0, bd=0, font=("Helvetica", 10))
            style.configure("Custom.Treeview.Heading", font=("Helvetica", 13, "bold"))
            table.place(x=10,y=85)

        def selected_options2_user(event):
            options2 = recherche_option.get()
            return options2

        def rechercher_par_ID_user():
            table.delete(*table.get_children())
            options_choisi = selected_options2_user(None)
            if options_choisi:
                ID = recherche_entry.get()
                admin = Admin()
                elem = admin.afficher_user_id(ID)
                tab = []
                for i in elem:
                    tab.append(i)
                table.insert("","end",values=(tab[0],tab[1],tab[2],tab[3],tab[4],tab[5],tab[6],tab[7],tab[8],tab[9]))

            def modifier_user():
                var_nom,var_prenom,var_age,var_numero,var_adresse,var_expiration,var_categorie = StringVar(),StringVar(),IntVar(),StringVar(),StringVar(),StringVar(),StringVar()

                def updating_properties_user():
                    conn = sqlite3.connect("biblio.db")
                    cursor = conn.cursor()
                    query = f"UPDATE u_tables SET nom=?,prenom=?,age=?,numero=?,adresse=?,expiration=?,categorie=? WHERE id=?"
                    cursor.execute(query,(
                        nom_user_entry.get(),
                        prenom_user_entry.get(),
                        age_user_entry.get(),
                        numero_user_entry.get(),
                        adresse_user_entry.get(),
                        expiration_user_entry.get(),
                        categorie_user_entry.get(),
                        ID))
                    conn.commit()
                    messagebox.showinfo("Modification","la modification à été bien prise en compte")
                    home_user_main()
                    conn.close()
                
                font1 = ctk.CTkFont(size=14)

                nom_user_label = ctk.CTkLabel(canvas1,text="Nom :",text_color="black",font=font1)
                nom_user_label.place(x=10,y=200)
                var_nom.set(tab[1])
                nom_user_entry = ctk.CTkEntry(canvas1,textvariable=var_nom)
                nom_user_entry.place(x=200,y=200)

                prenom_user_label = ctk.CTkLabel(canvas1,text="auteur :",text_color="black",font=font1)
                prenom_user_label.place(x=10,y=240)
                var_prenom.set(tab[2])
                prenom_user_entry = ctk.CTkEntry(canvas1,textvariable=var_prenom)
                prenom_user_entry.place(x=200,y=240)


                age_user_label = ctk.CTkLabel(canvas1,text="Age :",text_color="black",font=font1)
                age_user_label.place(x=10,y=280)
                var_age.set(tab[3])
                age_user_entry = ctk.CTkEntry(canvas1,textvariable=var_age)
                age_user_entry.place(x=200,y=280)
            

                numero_user_label = ctk.CTkLabel(canvas1,text="Numéro de téléphone :",text_color="black",font=font1)
                numero_user_label.place(x=10,y=320)
                var_numero.set(tab[5])
                numero_user_entry = ctk.CTkEntry(canvas1,textvariable=var_numero)
                numero_user_entry.place(x=200,y=320)


                adresse_user_label = ctk.CTkLabel(canvas1,text="Adresse du membre:",text_color="black",font=font1)
                adresse_user_label.place(x=10,y=360)
                var_adresse.set(tab[6])
                adresse_user_entry = ctk.CTkEntry(canvas1,textvariable=var_adresse)
                adresse_user_entry.place(x=200,y=360)

                expiration_user_label = ctk.CTkLabel(canvas1,text="date d'expiration :",text_color="black",font=font1)
                expiration_user_label.place(x=10,y=400)
                var_expiration.set(tab[7])
                expiration_user_entry = ctk.CTkEntry(canvas1,textvariable=var_expiration)
                expiration_user_entry.place(x=200,y=400)

                categorie_user_label = ctk.CTkLabel(canvas1,text="catégorie du membre :",text_color="black",font=font1)
                categorie_user_label.place(x=10,y=440)
                var_categorie.set(tab[8])
                categorie_list = ["gratuite","payante","etudiants","enfants","visiteurs"]
                categorie_user_entry = ctk.CTkComboBox(canvas1,values=categorie_list)
                categorie_user_entry.place(x=200,y=440)

            
                update_button = ctk.CTkButton(canvas1,text="Enregistrer la modification",command=updating_properties_user,fg_color="blue")
                update_button.place(x=55,y=480)

                # def enter(event):
                #     update_button.place(x=300, y=280)

                # update_button.bind("<Leave>",enter)
            
            def supprimer_ce_user():
                ID = recherche_entry.get()
                admin = Admin()
                if messagebox.askokcancel("supression","voulez-vous vraiment supprimer cette utilisateur ?"):
                    if messagebox.askokcancel("supression définitive","non mais t'es pas sérieux, mais tu vas vraiment tej ce membre ?"):
                        admin.supprimer_user(ID)

            modif = tk.Button(canvas1,text="Modifier ce membre",command=modifier_user)
            modif.place(x=10,y=140)
            delete = tk.Button(canvas1,text="Supprimer ce membre",command=supprimer_ce_user)
            delete.place(x=220,y=140)
            delete.config(bg="orange")
            



        def home_main():
            global search,l1,searching,show_all_button,recherche_entry,recherche_button,recherche_label,table
            search = tk.Frame(canvas1,width=1143,height=65)
            search.place(x=10,y=10)
            l1 = tk.Label(canvas1,text="Chercher une livre",fg="black",font=("Arial",11,"bold"))
            l1.place(x=40,y=10)

            values = ["ID","titre","auteur","annee","nombre","stock"]


            recherche_label = ttk.Combobox(canvas1,text="Rechercher :",values=values)
            recherche_label.bind("<<ComboboxSelected>>",selected_options)
            recherche_label.set("Afficher par")
            recherche_label.place(x=50,y=37)
            recherche_entry = tk.Entry(canvas1)
            recherche_entry.place(x=250,y=36)
            recherche_button = tk.Button(canvas1,text="rechercher",width=7,command=rechercher_livre)
            recherche_button.place(x=440,y=30)
            show_all_button = tk.Button(canvas1,text="Afficher tout",width=8,command=vraiment_afficher_tout)
            show_all_button.place(x=540,y=30)

            search_icon = tk.PhotoImage(file=ASSETS_PATH / "search24.png")
            searching = tk.Label(canvas1,image=search_icon)
            searching.image = search_icon
            searching.place(x=10,y=10)

            table = ttk.Treeview(canvas1,columns=("col1","col2","col3","col4","col5","col6","col7","col8","col9","col10"),show="headings")
            table.configure(height=24)
            table.heading("col1",text="ID")
            table.heading("col2", text="Titre")
            table.heading("col3", text="Auteur")
            table.heading("col4", text="Annee")
            table.heading("col5", text="Nbre")
            table.heading("col6", text="stock")
            table.heading("col7", text="genre")
            table.heading("col8", text="langue")
            table.heading("col9", text="local")
            table.heading("col10", text="date")

            

            table.column("col1",width=50,anchor="center")
            table.column("col2",anchor="center")
            table.column("col3",anchor="center")
            table.column("col4",width=70,anchor="center")
            table.column("col5",width=70,anchor="center")
            table.column("col6",width=88,anchor="center")
            table.column("col7",width=88,anchor="center")
            table.column("col8",width=88,anchor="center")
            table.column("col9",width=88,anchor="center")
            table.column("col10",anchor="center")


            table.configure(style="Custom.Treeview")

            style = ttk.Style()
            style.configure("Custom.Treeview", highlightthickness=0, bd=0, font=("Helvetica", 10))
            style.configure("Custom.Treeview.Heading", font=("Helvetica", 13, "bold"))
            table.place(x=10,y=85)

        def selected_options(event):
            options = recherche_label.get()
            return options


        def vraiment_afficher_tout():
            conn = sqlite3.connect("biblio.db")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM b_tables")
            rows = cursor.fetchall()
            table.delete(*table.get_children())
            for row in rows:
                id,titre,auteur,annee,nombre,stock,genre,langue,emplacement,date = (row[0]),(row[1]),(row[2]),(row[3]),(row[4]),(row[5]),(row[6]),(row[7]),(row[8]),(row[9])
                table.insert("", "end", values=(id, titre, auteur,annee,nombre,stock,genre,langue,emplacement,date))
            conn.close()

        def rechercher_livre():
            table.delete(*table.get_children())
            def verify_options():
                global options
                options = selected_options(None)
                different_options = ["ID","titre","auteur","annee","nombre","stock"]
                if options in different_options:
                    print(options)
                else:
                    options = "ID"    
                return options
            options = verify_options()
            print(options)
                
            titre_recherche = recherche_entry.get()
            conn = sqlite3.connect("biblio.db")
            cursor = conn.cursor()
            result = cursor.execute(f"SELECT * FROM b_tables WHERE titre LIKE ? ORDER BY {options}",('%' + titre_recherche + '%',))
            row1 = result.fetchall()
            
            if row1 is not None:
                for row in row1:
                    id,titre,auteur,annee,nombre,stock,genre,langue,local,date = (row[0]),(row[1]),(row[2]),(row[3]),(row[4]),(row[5]),(row[6]),(row[7]),(row[8]),(row[9])
                    table.insert("","end", values=(id,titre,auteur,annee,nombre,stock,genre,langue,local,date))
                    conn.close()
            else:
                table.destroy()
                error_label = tk.Label(canvas, text="Aucune correspondance",font=("Helvetica",13),fg="red",bg="#fff")        
                error_label.place(x=175,y=190)
                print("Aucune résultat trouvé")

        def adding_main():
            table.destroy()
            global search,titre,titre_entry,auteur,auteur_entry,annee,annee_combobox
            search = tk.Frame(canvas1,width=1160,height=550)
            search.place(x=10,y=10)

            font1 = ctk.CTkFont(size=14)
            
            titre = ctk.CTkLabel(search,text="Titre du livre               ",text_color="black",font=font1)
            titre.place(x=20,y=60)
            titre_entry = ctk.CTkEntry(search,width=170,height=35,border_color="#00a6d8",fg_color="#fff",text_color="black")
            titre_entry.place(x=400,y=55)

            auteur = ctk.CTkLabel(search,text="Auteur du livre             ",text_color="black",font=font1)
            auteur.place(x=20,y=110)
            auteur_entry = ctk.CTkEntry(search,width=170,height=35,border_color="#00a6d8",fg_color="#fff",text_color="black")
            auteur_entry.place(x=400,y=105)

            annee = ctk.CTkLabel(search,text="Année de sortie           ",text_color="black",font=font1)
            annee.place(x=20,y=160)

            tab = []
            for i in range(2000,2024):
                tab.append(str(i))
                

            annee_combobox = ctk.CTkComboBox(master=search,border_color="#00a6d8",fg_color="#fff",text_color="black",values=tab,dropdown_fg_color="white",dropdown_text_color="black",dropdown_hover_color="#00a6d8",button_color="#00a6d8")
            annee_combobox.place(x=400,y=155)   

            nombre = ctk.CTkLabel(search,text="Nombre d'exemplaire ",text_color="black",font=font1)
            nombre.place(x=20,y=215)
            nombre_entry = ctk.CTkEntry(search,width=100,height=35,border_color="#00a6d8",fg_color="#fff",text_color="black")
            nombre_entry.place(x=400,y=205)

            genre_liste = ["Fiction","Romance","Science-fiction","Fantasy","Policier/mystère","Thriller","Horreur","Poésie","Historique","jeunesse enfants","Éducation","for kids"]

            genre = ctk.CTkLabel(search,text="Genre du livre           ",text_color="black",font=font1)
            genre.place(x=20,y=260)
            genre_combobox = ctk.CTkComboBox(master=search,border_color="#00a6d8",fg_color="#fff",text_color="black",values=genre_liste,dropdown_fg_color="white",dropdown_text_color="black",dropdown_hover_color="#00a6d8",button_color="#00a6d8")
            genre_combobox.place(x=400,y=255)

            langue_liste = ["Français","Anglais","Malagasy"]

            langue = ctk.CTkLabel(search,text="Langue du livre           ",text_color="black",font=font1)
            langue.place(x=20,y=310)
            langue_combobox = ctk.CTkComboBox(master=search,border_color="#00a6d8",fg_color="#fff",text_color="black",values=langue_liste,dropdown_fg_color="white",dropdown_text_color="black",dropdown_hover_color="#00a6d8",button_color="#00a6d8")
            langue_combobox.place(x=400,y=305)

            emplacement_liste = ["FCT1","RMN1","SCF1","FAN1","PO/M1","THR1","HRR1","POE1","HIST1","ED1"]

            emplacement = ctk.CTkLabel(search,text="Emplacement physique             ",text_color="black",font=font1)
            emplacement.place(x=20,y=360)
            emplacement_combobox = ctk.CTkComboBox(master=search,border_color="#00a6d8",fg_color="#fff",text_color="black",values=emplacement_liste,dropdown_fg_color="white",dropdown_text_color="black",dropdown_hover_color="#00a6d8",button_color="#00a6d8")
            emplacement_combobox.place(x=400,y=355)


            def get_id():
                conn = sqlite3.connect("biblio.db")
                conn.commit()
                cursor = conn.cursor()
                try:
                    cursor.execute("SELECT id FROM b_tables ORDER BY id DESC LIMIT 1")
                    row = cursor.fetchone()
                    if row is not None:
                        last_id = row[0]
                    conn.close()
                    return last_id
                except:
                    last_id = 0
                    return last_id
    


            def ajout_livres():
                last_id = get_id()
                new_id = last_id + 1
                titre = titre_entry.get()
                auteur = auteur_entry.get()
                annee = annee_combobox.get()
                nombre = nombre_entry.get()
                genre = genre_combobox.get()
                langue = langue_combobox.get()
                emplacement = emplacement_combobox.get()
                stock = nombre
                if titre and auteur and annee and nombre and genre and langue and emplacement:
                    bibliotheque = Bibliotheque()
                    livre = Livre(new_id, titre, auteur, annee, nombre, stock,genre,langue,emplacement,date=show_date())
                    bibliotheque.ajouter_livre(livre)
                    home_book()
                else:
                    messagebox.showerror("Champs incomplet","veuillez vérifiéz que tous les champs soient remplissent")

            submit = ctk.CTkButton(master=search,fg_color=("white","#00a6d8"),text="Enregistrer",command=ajout_livres)
            submit.place(x=20,y=405)
              

            
        
        def update_main():
            global recherche_option,recherche_entry,table,tab1,recherche_button,search
            search = tk.Frame(canvas1,width=1143,height=70)
            search.place(x=10,y=10)

            # tab1 = tk.Frame(canvas,width=1143,height=320)
            # tab1.place(x=170,y=190)


            l1 = tk.Label(search,text="Chercher une livre par ID",fg="black",font=("Arial",11,"bold"))
            l1.place(x=30,y=4)
            search_icon = tk.PhotoImage(file=ASSETS_PATH / "seach24.png")
            searching = tk.Label(search,image=search_icon)
            searching.image = search_icon
            searching.place(x=0,y=4)

            values = ["ID"]

            recherche_option  = ttk.Combobox(search,text="Chercher par:",values=values)
            recherche_option.bind("<<ComboboxSelected>>",selected_options2)
            recherche_option.set("Rechercher par")
            recherche_option.place(x=50,y=30)

            recherche_entry = tk.Entry(search)
            recherche_entry.place(x=240,y=29)
            recherche_button = tk.Button(search,text="rechercher",width=7,command=rechercher_par_ID)
            recherche_button.place(x=450,y=27)
            # show_all_button = tk.Button(search,text="Afficher tout",width=8,command=vraiment_afficher_tout)
            # show_all_button.place(x=550,y=26)

            table = ttk.Treeview(canvas1,columns=("col1","col2","col3","col4","col5","col6","col7","col8","col9","col10"),show="headings")
            table.configure(height=1)
            table.heading("col1",text="ID")
            table.heading("col2", text="Titre")
            table.heading("col3", text="Auteur")
            table.heading("col4", text="Annee")
            table.heading("col5", text="Nbre")
            table.heading("col6", text="stock")
            table.heading("col7", text="genre")
            table.heading("col8", text="langue")
            table.heading("col9", text="local")
            table.heading("col10", text="date")

            

            table.column("col1",width=50,anchor="center")
            table.column("col2",anchor="center")
            table.column("col3",anchor="center")
            table.column("col4",width=70,anchor="center")
            table.column("col5",width=70,anchor="center")
            table.column("col6",width=88,anchor="center")
            table.column("col7",width=88,anchor="center")
            table.column("col8",width=88,anchor="center")
            table.column("col9",width=88,anchor="center")
            table.column("col10",anchor="center")


            table.configure(style="Custom.Treeview")

            style = ttk.Style()
            style.configure("Custom.Treeview", highlightthickness=0, bd=0, font=("Helvetica", 10))
            style.configure("Custom.Treeview.Heading", font=("Helvetica", 13, "bold"))
            table.place(x=10,y=85)
              
        

        def selected_options2(event):
            options2 = recherche_option.get()
            return options2
        
        def rechercher_par_ID():
            table.delete(*table.get_children())
            options_choisi = selected_options2(None)
            if options_choisi:
                ID = recherche_entry.get()
                admin = Bibliotheque()
                elem = admin.afficher_livre_id(ID)
                tab = []
                for i in elem:
                    tab.append(i)
                table.insert("","end",values=(tab[0],tab[1],tab[2],tab[3],tab[4],tab[5],tab[6],tab[7],tab[8],tab[9]))


            def modifier_livre():
                global titre_livre,titre_entry,auteur_livre,auteur_entry,nombre_livre,nombre_entry,stock_livre,stock_entry,annee_livre,annee_entry,update_button,cancel_button
                var_titre,var_auteur,var_annee,var_nombre,var_stock = StringVar(),StringVar(),IntVar(),IntVar(),IntVar()

                def updating_properties():
                    
                    conn = sqlite3.connect("biblio.db")
                    cursor = conn.cursor()
                    query = f"UPDATE b_tables SET titre=?,auteur=?,annee=?,nombre=?,stock=? WHERE id=?"
                    cursor.execute(query,(titre_entry.get(),auteur_entry.get(),annee_entry.get(),nombre_entry.get(),stock_entry.get(),ID))
                    conn.commit()
                    messagebox.showinfo("Modification","la modification à été bien prise en compte")
                    print("Le livre à bien été modifié")
                    titre_livre.destroy()
                    titre_entry.destroy()
                    auteur_livre.destroy()
                    auteur_entry.destroy()
                    annee_livre.destroy()
                    annee_entry.destroy()
                    nombre_livre.destroy()
                    nombre_entry.destroy()
                    stock_livre.destroy()
                    stock_entry.destroy()
                    update_button.destroy()
                    update_main()
                    conn.close()

                font1 = ctk.CTkFont(size=14)

                titre_livre = ctk.CTkLabel(canvas1,text="titre ",text_color="black",font=font1)
                titre_livre.place(x=10,y=200)
                var_titre.set(tab[1])
                titre_entry = ctk.CTkEntry(canvas1,textvariable=var_titre)
                titre_entry.place(x=87,y=200)

                auteur_livre = ctk.CTkLabel(canvas1,text="auteur ",text_color="black",font=font1)
                auteur_livre.place(x=10,y=240)
                var_auteur.set(tab[2])
                auteur_entry = ctk.CTkEntry(canvas1,textvariable=var_auteur)
                auteur_entry.place(x=87,y=240)

                annee_livre = ctk.CTkLabel(canvas1,text="annee ",text_color="black",font=font1)
                annee_livre.place(x=10,y=280)
                var_annee.set(tab[3])
                annee_entry = ctk.CTkEntry(canvas1,textvariable=var_annee)
                annee_entry.place(x=87,y=280)

                nombre_livre = ctk.CTkLabel(canvas1,text="nombre ",text_color="black",font=font1)
                nombre_livre.place(x=10,y=320)
                var_nombre.set(tab[4])
                nombre_entry = ctk.CTkEntry(canvas1,textvariable=var_nombre)
                nombre_entry.place(x=87,y=320)

                stock_livre = ctk.CTkLabel(canvas1,text="stock ",text_color="black",font=font1)
                stock_livre.place(x=10,y=360)
                var_stock.set(tab[4])
                stock_entry = ctk.CTkEntry(canvas1,textvariable=var_stock)
                stock_entry.place(x=87,y=360)

                update_button = tk.Button(canvas1,text="Enregistrer la modification",command=updating_properties)
                update_button.place(x=10,y=400)

                cancel_button = tk.Button(canvas1,text="Annuler",command=update_book,fg="red")
                cancel_button.place(x=300,y=400)
                
            def cancel():
                titre_livre.destroy()
                titre_entry.destroy()
                auteur_livre.destroy()
                auteur_entry.destroy()
                annee_livre.destroy()
                annee_entry.destroy()
                nombre_livre.destroy()
                nombre_entry.destroy()
                stock_livre.destroy()
                stock_entry.destroy()
                update_button.destroy()
                cancel_button.destroy()
                modif.destroy()
                delete.destroy()
    
            def supprimer_ce_livre():
                ID = recherche_entry.get()
                admin = Bibliotheque()
                if messagebox.askokcancel("supression","voulez-vous vraiment supprimer ce livre ?"):
                    if messagebox.askokcancel("supression définitive","non mais t'es pas sérieux, mais vraiment tu vas supprimé ce livre ?"):
                        admin.supprimer_livre(ID)

            modif = tk.Button(canvas1,text="Modifier ce livre",command=modifier_livre)
            modif.place(x=10,y=140)
            delete = tk.Button(canvas1,text="Supprimer ce livre",command=supprimer_ce_livre)
            delete.place(x=220,y=140)
            delete.config(bg="orange")
        home_main()
    menu()
    window.mainloop()
