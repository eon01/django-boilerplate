mv boilerplate/boilerplate/ boilerplate/$1
mv boilerplate $1
pip install -r $1/requirements.txt
find . -type f  -exec sed -i 's/boilerplate/'"$1"'/g' {} +
mv $1/var.env $1/.env
mv db/var.env db/.env
mv dbadmin/var.env dbadmin/.env
# rm -rf .git 
# git init