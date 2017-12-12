echo "$1 is the url" 
echo "$2 is the commit sha" 

cd /Users/kshitijbhatnagar/Desktop/Cyclometric complexity/SubData

rm -rf .git/

git init

git remote add origin $1

git pull