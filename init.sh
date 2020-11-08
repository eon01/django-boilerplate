mv boilerplate/boilerplate/ boilerplate/$1
mv boilerplate $1
pip install -r $1/requirements.txt
find . -type f  -exec sed -i 's/boilerplate/$1/g' {} +


