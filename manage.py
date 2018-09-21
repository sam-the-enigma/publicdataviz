import argparse
import os
import subprocess
import virtualenv

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
        flask_env = os.environ.copy()
        flask_env['FLASK_APP'] = 'backend/app.py'
        subprocess.Popen(['./venv/bin/python', '-m', 'flask', 'run'], env=flask_env).communicate()
    except KeyboardInterrupt:
        exit(0)


def run_frontend():
    print('Launching frontend')
    try:
        subprocess.Popen(['npm', '--prefix', './frontend', 'start']).communicate()
    except KeyboardInterrupt:
        exit(0)


def install():
    print("Installing")
    install_backend()
    install_frontend()
    print("Installation complete. Exiting")


def install_backend():
    print("Installing backend")
    venv_dir = './venv'
    create_and_source_virtual_environment(venv_dir)
    install_python_dependencies(venv_dir)
    print("Backend installed")

def install_frontend():
    print("Installing frontend")
    subprocess.call(['npm', '--prefix', './frontend', 'install'])


def create_and_source_virtual_environment(venv_dir):
    print("Creating virtual environment")
    os.mkdir(venv_dir)
    virtualenv.create_environment(venv_dir, site_packages=False)

    print("Sourcing virtual environment")
    source_script = os.path.join(venv_dir, "bin", "activate_this.py")

    with open(source_script) as f:
        exec(f.read(), {'__file__': source_script})
        

def install_python_dependencies(venv_dir):
    print("Installing python dependencies into virtual environment")
    subprocess.call(['pip', 'install', '-r', 'backend/requirements.txt'])


if __name__ == '__main__':
    main()
