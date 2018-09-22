import argparse
import os
import subprocess
import virtualenv

pyname = 'py' if os.name == 'nt' else 'python'

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('mode')
    args = ap.parse_args()

    if args.mode == 'install':
        install()
    elif args.mode == 'run-backend':
        run_backend()
    elif args.mode == 'run-frontend':
        run_frontend()
    else:
        print('Unknown mode. Acceptable options: install | run_backend | run_frontend')

def run_backend():
    print('Launching backend')
    try:
        source_virtualenv(f'.{os.sep}venv')
        flask_env = os.environ.copy()
        flask_env['FLASK_APP'] = 'backend/app.py'
        subprocess.Popen([pyname, '-m', 'flask', 'run'], env=flask_env).communicate()
    except KeyboardInterrupt:
        exit(0)


def run_frontend():
    print('Launching frontend')
    try:
        if pyname == 'py':
            subprocess.Popen('cd ./frontend && npm start', shell=True).communicate()
        else:
            subprocess.Popen(['npm', '--prefix', f'frontend/', 'start']).communicate()
    except KeyboardInterrupt:
        exit(0)


def install():
    print("Installing")
    install_backend()
    install_frontend()
    print("Installation complete. Exiting")


def install_backend():
    print("Installing backend")
    venv_dir = f'.{os.sep}venv'
    create_and_source_virtual_environment(venv_dir)
    install_python_dependencies(venv_dir)
    print("Backend installed")

def install_frontend():
    print("Installing frontend")
    if pyname == 'py':
        subprocess.call('cd ./frontend && npm install', shell=True)
    else:
        subprocess.call(['npm', '--prefix', 'frontend/', 'install'])


def create_and_source_virtual_environment(venv_dir):
    print("Creating virtual environment")
    os.mkdir(venv_dir)
    virtualenv.create_environment(venv_dir, site_packages=False)
    source_virtualenv(venv_dir)
    
        

def install_python_dependencies(venv_dir):
    print("Installing python dependencies into virtual environment")
    if pyname == 'python':
        subprocess.call(['pip', 'install', '-r', 'backend/requirements.txt'])
    else:
        subprocess.call(['py', '-m', 'pip', 'install', '-r', 'backend/requirements.txt'])


def source_virtualenv(venv_dir):
    print("Sourcing virtual environment")
    source_script = os.path.join(venv_dir, 'Scripts' if pyname == 'py' else 'bin', 'activate_this.py')

    with open(source_script) as f:
        exec(f.read(), {'__file__': source_script})


if __name__ == '__main__':
    main()
