from multiprocessing import Pool
from pathlib import Path
import os, glob, shutil, time
from datetime import datetime


def process_line(line):
    #se connecter a la database ici
    return line

def move_files(file):
    new_url = "_performedFiles/" + file
    Path(file).rename(new_url)

def zip_processed(foler):
    output_name = datetime.now().strftime("%Y%m%d_%H%M%S") + "_archive"
    shutil.make_archive(output_name, 'zip', "_performedFiles/")

def delete_zipped_files():
    dir = '/Users/thomasjaulgey/Documents/_TSE_IUT/_FISA_DE/_DE3/_DEV/_MultiThread/_Projet/_performedFiles/'
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))



if __name__ == "__main__":
    #declaration des pools de thread
    pool = Pool(4)


    while True:
        #dossier de travail (a modifier)
        path = "/Users/thomasjaulgey/Documents/_TSE_IUT/_FISA_DE/_DE3/_DEV/_MultiThread/_Projet"
        
        #seulement garder les csv dans  exploration fichiers
        extension = 'csv'

        os.chdir(path)
        dir_list = glob.glob('*.{}'.format(extension))
            
        for i in dir_list:
            with open(i) as source_file:
                #recuperer toutes les lignes de chaque fichier pour import en BDD
                results = pool.map(process_line, source_file)        
            
        #deplacer les fichiers traités
        pool.map(move_files, dir_list)

        #zip et suppression des fichiers
        folder = "/Users/thomasjaulgey/Documents/_TSE_IUT/_FISA_DE/_DE3/_DEV/_MultiThread/_Projet/__performedFiles"
        pool.map(zip_processed, folder)
        pool.apply(delete_zipped_files)

        #on boucle sur ce programme toutes les 5 secondes (pour lancer le processus régulièrement)
        time.sleep(5)
    
    

