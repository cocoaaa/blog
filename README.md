# Do everything regarding the changes in blog, do everything
# at the source branch
# To publish locally
make html && make serve
# check on http://localhost:8000/:

# To publish
git checkout source
ghp-import -b master output/
git push origin master
 

