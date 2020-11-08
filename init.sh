mv boilerplate/boilerplate/ boilerplate/$1
mv boilerplate $1
find . -type f  -exec sed -i 's/boilerplate/$1/g' {} +


