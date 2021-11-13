sudo apt install python3 python3-pip python3-venv -y

python3 -m venv venv
source venv/bin/activate

pip3 install -r requirements.txt

while getopts "c" options; do
  case ${options} in
    c) create=true;;
  esac
done

if [ ${create} ]; then
  python3 create.py
fi

python3 app.py