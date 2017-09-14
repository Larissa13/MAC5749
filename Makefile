# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line
GH_PAGES_SOURCES = docs/source sarpy Makefile docs/images
SPHINXOPTS    = 
SPHINXBUILD   = python -msphinx
SPHINXPROJ    = sarpydocs
SOURCEDIR     = docs/source
BUILDDIR      = build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
html: Makefile
	rm -f docs/source/*.rst
	sphinx-apidoc -fe -o docs/source sarpy
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
''
gh-pages:
	git checkout gh-pages
	rm -rf {build,_static,images,_sources,.nojekyll}
	git checkout master $(GH_PAGES_SOURCES)
	git reset HEAD
	make html
	mv docs/images .
	mv -fv build/html/* ./
	mv sarpy.html index.html
	rm -rf $(GH_PAGES_SOURCES) build
	touch .nojekyll
	git add -A
	git commit -m "Generated gh-pages for `git log master -1 --pretty=short --abbrev-commit`" && git push origin gh-pages ; git checkout master 
	echo "Finished Deployment!"