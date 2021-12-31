#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-RaschSampler
Version  : 0.8.8
Release  : 29
URL      : https://cran.r-project.org/src/contrib/RaschSampler_0.8-8.tar.gz
Source0  : https://cran.r-project.org/src/contrib/RaschSampler_0.8-8.tar.gz
Summary  : Rasch Sampler
Group    : Development/Tools
License  : GPL-2.0
Requires: R-RaschSampler-lib = %{version}-%{release}
BuildRequires : buildreq-R

%description
No detailed description available

%package lib
Summary: lib components for the R-RaschSampler package.
Group: Libraries

%description lib
lib components for the R-RaschSampler package.


%prep
%setup -q -c -n RaschSampler
cd %{_builddir}/RaschSampler

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1589524410

%install
export SOURCE_DATE_EPOCH=1589524410
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library RaschSampler
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library RaschSampler
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library RaschSampler
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc RaschSampler || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/RaschSampler/DESCRIPTION
/usr/lib64/R/library/RaschSampler/INDEX
/usr/lib64/R/library/RaschSampler/Meta/Rd.rds
/usr/lib64/R/library/RaschSampler/Meta/data.rds
/usr/lib64/R/library/RaschSampler/Meta/features.rds
/usr/lib64/R/library/RaschSampler/Meta/hsearch.rds
/usr/lib64/R/library/RaschSampler/Meta/links.rds
/usr/lib64/R/library/RaschSampler/Meta/nsInfo.rds
/usr/lib64/R/library/RaschSampler/Meta/package.rds
/usr/lib64/R/library/RaschSampler/NAMESPACE
/usr/lib64/R/library/RaschSampler/R/RaschSampler
/usr/lib64/R/library/RaschSampler/R/RaschSampler.rdb
/usr/lib64/R/library/RaschSampler/R/RaschSampler.rdx
/usr/lib64/R/library/RaschSampler/data/xmpl.rda
/usr/lib64/R/library/RaschSampler/data/xmplbig.rda
/usr/lib64/R/library/RaschSampler/help/AnIndex
/usr/lib64/R/library/RaschSampler/help/RaschSampler.rdb
/usr/lib64/R/library/RaschSampler/help/RaschSampler.rdx
/usr/lib64/R/library/RaschSampler/help/aliases.rds
/usr/lib64/R/library/RaschSampler/help/paths.rds
/usr/lib64/R/library/RaschSampler/html/00Index.html
/usr/lib64/R/library/RaschSampler/html/R.css

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/RaschSampler/libs/RaschSampler.so
