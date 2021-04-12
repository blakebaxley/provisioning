from flask import Flask, request
import os
import shutil
import subprocess

app = Flask(__name__)

@app.route('/')
def hello():
    return "e11y provisioning tool: hit /e11y/createSchema with sName : accountId in the body of your post to provision a new schema\n"

@app.route('/e11y/api/createSchema', methods=['POST'])
def create():

    aid = request.json['sName']
    schema_name = "e11y_"+str(aid)
    load_schema(schema_name)
    return 'success\n'
@app.route('/e11y/api/deleteSchema', methods=['POST'])
def delete():

    aid = request.json['sName']
    schema_name = "e11y_"+str(aid)
    del_schema(schema_name)
    return 'success\n'

def load_schema(schema_name):
    schema = schema_name
    sql_files = os.listdir('elly_schema')
    create_path = "../skeema_files/localhost/{0}".format(schema)
    print(create_path)
    mkdir(create_path)
    for file_name in sql_files:
        full_file_name = os.path.join('elly_schema', file_name)
        if os.path.isfile(full_file_name):
            shutil.copy(full_file_name, create_path)
    gen_skeema_file(create_path, schema)
    command = ['skeema', 'push', '-uskeema', '-pPardot07']
    subprocess.Popen(command, cwd='../skeema_files')

def del_schema(schema_name):
    schema = schema_name
    sql_files = os.listdir('elly_schema')
    del_path = "../skeema_files/localhost/{0}".format(schema)
    print(del_path)
    for file_name in sql_files:
        full_file_name = os.path.join(del_path, file_name)
        print(full_file_name)
        if os.path.isfile(full_file_name):
            delfile(full_file_name)
    command = ['skeema', 'push', '-uskeema', '-pPardot07', '--allow-unsafe']
    subprocess.Popen(command, cwd='../skeema_files')

def mkdir(path):
    try:
        os.makedirs(path)
    except OSError as exc:
        if not os.path.isdir(path):
            raise

def deldir(path):
    try:
        shutil.rmtree(path)
    except OSError as exc:
        if os.path.isdir(path):
            raise

def delfile(path):
    try:
        os. remove(path)
    except OSError as exc:
        if os.path.isfile(path):
            raise


def gen_skeema_file(path, schema):
    file_name = path + "/.skeema"
    f = open(file_name, "a")
    f.write("default-character-set=utf8mb4\n")
    f.write("default-collation=utf8mb4_0900_ai_ci\n")
    f.write("schema=" + schema)
    f.close()

if __name__ == '__main__':
       app.run()