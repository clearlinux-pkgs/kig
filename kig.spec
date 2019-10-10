#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : kig
Version  : 19.08.2
Release  : 15
URL      : https://download.kde.org/stable/applications/19.08.2/src/kig-19.08.2.tar.xz
Source0  : https://download.kde.org/stable/applications/19.08.2/src/kig-19.08.2.tar.xz
Source1 : https://download.kde.org/stable/applications/19.08.2/src/kig-19.08.2.tar.xz.sig
Summary  : Interactive Geometry
Group    : Development/Tools
License  : BSD-3-Clause GFDL-1.2 GPL-2.0
Requires: kig-bin = %{version}-%{release}
Requires: kig-data = %{version}-%{release}
Requires: kig-lib = %{version}-%{release}
Requires: kig-license = %{version}-%{release}
Requires: kig-locales = %{version}-%{release}
Requires: kig-man = %{version}-%{release}
BuildRequires : boost-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : ktexteditor-dev
BuildRequires : pkg-config
BuildRequires : python3-dev

%description
Kig v@KIGVERSION@
Kig developers <kde-edu-devel@kde.org>
----------------------------------------------------------------------
Kig: KDE Interactive Geometry
Kig is a program for use in math classes in high school, to allow
students to interactively explore geometric concepts.  For more
information: check out the documentation ( open "help:/kig" in
konqueror...)

%package bin
Summary: bin components for the kig package.
Group: Binaries
Requires: kig-data = %{version}-%{release}
Requires: kig-license = %{version}-%{release}

%description bin
bin components for the kig package.


%package data
Summary: data components for the kig package.
Group: Data

%description data
data components for the kig package.


%package doc
Summary: doc components for the kig package.
Group: Documentation
Requires: kig-man = %{version}-%{release}

%description doc
doc components for the kig package.


%package lib
Summary: lib components for the kig package.
Group: Libraries
Requires: kig-data = %{version}-%{release}
Requires: kig-license = %{version}-%{release}

%description lib
lib components for the kig package.


%package license
Summary: license components for the kig package.
Group: Default

%description license
license components for the kig package.


%package locales
Summary: locales components for the kig package.
Group: Default

%description locales
locales components for the kig package.


%package man
Summary: man components for the kig package.
Group: Default

%description man
man components for the kig package.


%prep
%setup -q -n kig-19.08.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1570744665
mkdir -p clr-build
pushd clr-build
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1570744665
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kig
cp COPYING %{buildroot}/usr/share/package-licenses/kig/COPYING
cp COPYING.DOC %{buildroot}/usr/share/package-licenses/kig/COPYING.DOC
cp cmake/modules/COPYING-CMAKE-SCRIPTS %{buildroot}/usr/share/package-licenses/kig/cmake_modules_COPYING-CMAKE-SCRIPTS
pushd clr-build
%make_install
popd
%find_lang kfile_drgeo
%find_lang kfile_kig
%find_lang kig

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/kig
/usr/bin/pykig.py

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.kig.desktop
/usr/share/icons/hicolor/128x128/apps/kig.png
/usr/share/icons/hicolor/128x128/mimetypes/application-x-kig.png
/usr/share/icons/hicolor/16x16/apps/kig.png
/usr/share/icons/hicolor/16x16/mimetypes/application-x-kig.png
/usr/share/icons/hicolor/22x22/apps/kig.png
/usr/share/icons/hicolor/22x22/mimetypes/application-x-kig.png
/usr/share/icons/hicolor/32x32/apps/kig.png
/usr/share/icons/hicolor/32x32/mimetypes/application-x-kig.png
/usr/share/icons/hicolor/48x48/apps/kig.png
/usr/share/icons/hicolor/48x48/mimetypes/application-x-kig.png
/usr/share/icons/hicolor/64x64/apps/kig.png
/usr/share/icons/hicolor/64x64/mimetypes/application-x-kig.png
/usr/share/icons/hicolor/scalable/apps/kig.svgz
/usr/share/icons/hicolor/scalable/mimetypes/application-x-kig.svgz
/usr/share/kig/builtin-macros/circle_by_center_and_line.kigt
/usr/share/kig/builtin-macros/circle_by_point_and_diameter.kigt
/usr/share/kig/builtin-macros/equitriangle.kigt
/usr/share/kig/builtin-macros/evolute.kigt
/usr/share/kig/builtin-macros/osculating_circle.kigt
/usr/share/kig/builtin-macros/square.kigt
/usr/share/kig/builtin-macros/vector_difference.kigt
/usr/share/kig/icons/hicolor/16x16/actions/kig_xfig.png
/usr/share/kig/icons/hicolor/22x22/actions/angle.png
/usr/share/kig/icons/hicolor/22x22/actions/angle_bisector.png
/usr/share/kig/icons/hicolor/22x22/actions/angle_size.png
/usr/share/kig/icons/hicolor/22x22/actions/arc.png
/usr/share/kig/icons/hicolor/22x22/actions/arc_center.png
/usr/share/kig/icons/hicolor/22x22/actions/areaCircle.png
/usr/share/kig/icons/hicolor/22x22/actions/attacher.png
/usr/share/kig/icons/hicolor/22x22/actions/baseCircle.png
/usr/share/kig/icons/hicolor/22x22/actions/bezier3.png
/usr/share/kig/icons/hicolor/22x22/actions/bezier4.png
/usr/share/kig/icons/hicolor/22x22/actions/bezierN.png
/usr/share/kig/icons/hicolor/22x22/actions/beziercurves.png
/usr/share/kig/icons/hicolor/22x22/actions/bisection.png
/usr/share/kig/icons/hicolor/22x22/actions/centerofcurvature.png
/usr/share/kig/icons/hicolor/22x22/actions/centralsymmetry.png
/usr/share/kig/icons/hicolor/22x22/actions/circlebcl.png
/usr/share/kig/icons/hicolor/22x22/actions/circlebcp.png
/usr/share/kig/icons/hicolor/22x22/actions/circlebpd.png
/usr/share/kig/icons/hicolor/22x22/actions/circlebps.png
/usr/share/kig/icons/hicolor/22x22/actions/circlebtp.png
/usr/share/kig/icons/hicolor/22x22/actions/circlelineintersection.png
/usr/share/kig/icons/hicolor/22x22/actions/circumference.png
/usr/share/kig/icons/hicolor/22x22/actions/conicasymptotes.png
/usr/share/kig/icons/hicolor/22x22/actions/conicb5p.png
/usr/share/kig/icons/hicolor/22x22/actions/coniclineintersection.png
/usr/share/kig/icons/hicolor/22x22/actions/conicsradicalline.png
/usr/share/kig/icons/hicolor/22x22/actions/controlpolygon.png
/usr/share/kig/icons/hicolor/22x22/actions/convexhull.png
/usr/share/kig/icons/hicolor/22x22/actions/curvelineintersection.png
/usr/share/kig/icons/hicolor/22x22/actions/directrix.png
/usr/share/kig/icons/hicolor/22x22/actions/distance.png
/usr/share/kig/icons/hicolor/22x22/actions/ellipsebffp.png
/usr/share/kig/icons/hicolor/22x22/actions/en.png
/usr/share/kig/icons/hicolor/22x22/actions/equilateralhyperbolab4p.png
/usr/share/kig/icons/hicolor/22x22/actions/equitriangle.png
/usr/share/kig/icons/hicolor/22x22/actions/genericaffinity.png
/usr/share/kig/icons/hicolor/22x22/actions/genericprojectivity.png
/usr/share/kig/icons/hicolor/22x22/actions/halflinebyvector.png
/usr/share/kig/icons/hicolor/22x22/actions/harmonichomology.png
/usr/share/kig/icons/hicolor/22x22/actions/hexagonbcv.png
/usr/share/kig/icons/hicolor/22x22/actions/hyperbolabffp.png
/usr/share/kig/icons/hicolor/22x22/actions/intersection.png
/usr/share/kig/icons/hicolor/22x22/actions/inversion.png
/usr/share/kig/icons/hicolor/22x22/actions/kig_numericvalue.png
/usr/share/kig/icons/hicolor/22x22/actions/kig_polygon.png
/usr/share/kig/icons/hicolor/22x22/actions/kig_text.png
/usr/share/kig/icons/hicolor/22x22/actions/line.png
/usr/share/kig/icons/hicolor/22x22/actions/linebyvector.png
/usr/share/kig/icons/hicolor/22x22/actions/locus.png
/usr/share/kig/icons/hicolor/22x22/actions/mirrorpoint.png
/usr/share/kig/icons/hicolor/22x22/actions/openpolygon.png
/usr/share/kig/icons/hicolor/22x22/actions/paint.png
/usr/share/kig/icons/hicolor/22x22/actions/parabolabtp.png
/usr/share/kig/icons/hicolor/22x22/actions/parallel.png
/usr/share/kig/icons/hicolor/22x22/actions/perpendicular.png
/usr/share/kig/icons/hicolor/22x22/actions/point.png
/usr/share/kig/icons/hicolor/22x22/actions/pointOnLine.png
/usr/share/kig/icons/hicolor/22x22/actions/pointxy.png
/usr/share/kig/icons/hicolor/22x22/actions/polygonsides.png
/usr/share/kig/icons/hicolor/22x22/actions/polygonvertices.png
/usr/share/kig/icons/hicolor/22x22/actions/projection.png
/usr/share/kig/icons/hicolor/22x22/actions/python.png
/usr/share/kig/icons/hicolor/22x22/actions/radicalline.png
/usr/share/kig/icons/hicolor/22x22/actions/ray.png
/usr/share/kig/icons/hicolor/22x22/actions/rbezier3.png
/usr/share/kig/icons/hicolor/22x22/actions/rbezier4.png
/usr/share/kig/icons/hicolor/22x22/actions/rbezierN.png
/usr/share/kig/icons/hicolor/22x22/actions/rotation.png
/usr/share/kig/icons/hicolor/22x22/actions/scale.png
/usr/share/kig/icons/hicolor/22x22/actions/segment.png
/usr/share/kig/icons/hicolor/22x22/actions/segment_golden_point.png
/usr/share/kig/icons/hicolor/22x22/actions/segment_midpoint.png
/usr/share/kig/icons/hicolor/22x22/actions/segmentaxis.png
/usr/share/kig/icons/hicolor/22x22/actions/similitude.png
/usr/share/kig/icons/hicolor/22x22/actions/sizer.png
/usr/share/kig/icons/hicolor/22x22/actions/slope.png
/usr/share/kig/icons/hicolor/22x22/actions/square.png
/usr/share/kig/icons/hicolor/22x22/actions/stretch.png
/usr/share/kig/icons/hicolor/22x22/actions/tangent.png
/usr/share/kig/icons/hicolor/22x22/actions/test.png
/usr/share/kig/icons/hicolor/22x22/actions/testcollinear.png
/usr/share/kig/icons/hicolor/22x22/actions/testcontains.png
/usr/share/kig/icons/hicolor/22x22/actions/testdistance.png
/usr/share/kig/icons/hicolor/22x22/actions/testorthogonal.png
/usr/share/kig/icons/hicolor/22x22/actions/testparallel.png
/usr/share/kig/icons/hicolor/22x22/actions/translation.png
/usr/share/kig/icons/hicolor/22x22/actions/triangle.png
/usr/share/kig/icons/hicolor/22x22/actions/vector.png
/usr/share/kig/icons/hicolor/22x22/actions/vectordifference.png
/usr/share/kig/icons/hicolor/22x22/actions/vectorsum.png
/usr/share/kig/icons/hicolor/22x22/actions/view_fit_to_page.png
/usr/share/kig/icons/hicolor/22x22/actions/w.png
/usr/share/kig/icons/hicolor/32x32/actions/angle.png
/usr/share/kig/icons/hicolor/32x32/actions/angle_bisector.png
/usr/share/kig/icons/hicolor/32x32/actions/angle_size.png
/usr/share/kig/icons/hicolor/32x32/actions/arc.png
/usr/share/kig/icons/hicolor/32x32/actions/arc_center.png
/usr/share/kig/icons/hicolor/32x32/actions/areaCircle.png
/usr/share/kig/icons/hicolor/32x32/actions/attacher.png
/usr/share/kig/icons/hicolor/32x32/actions/baseCircle.png
/usr/share/kig/icons/hicolor/32x32/actions/bezier3.png
/usr/share/kig/icons/hicolor/32x32/actions/bezier4.png
/usr/share/kig/icons/hicolor/32x32/actions/bezierN.png
/usr/share/kig/icons/hicolor/32x32/actions/beziercurves.png
/usr/share/kig/icons/hicolor/32x32/actions/bisection.png
/usr/share/kig/icons/hicolor/32x32/actions/centerofcurvature.png
/usr/share/kig/icons/hicolor/32x32/actions/centralsymmetry.png
/usr/share/kig/icons/hicolor/32x32/actions/circlebcl.png
/usr/share/kig/icons/hicolor/32x32/actions/circlebcp.png
/usr/share/kig/icons/hicolor/32x32/actions/circlebpd.png
/usr/share/kig/icons/hicolor/32x32/actions/circlebps.png
/usr/share/kig/icons/hicolor/32x32/actions/circlebtp.png
/usr/share/kig/icons/hicolor/32x32/actions/circlelineintersection.png
/usr/share/kig/icons/hicolor/32x32/actions/circumference.png
/usr/share/kig/icons/hicolor/32x32/actions/conicasymptotes.png
/usr/share/kig/icons/hicolor/32x32/actions/conicb5p.png
/usr/share/kig/icons/hicolor/32x32/actions/coniclineintersection.png
/usr/share/kig/icons/hicolor/32x32/actions/conicsradicalline.png
/usr/share/kig/icons/hicolor/32x32/actions/controlpolygon.png
/usr/share/kig/icons/hicolor/32x32/actions/convexhull.png
/usr/share/kig/icons/hicolor/32x32/actions/curvelineintersection.png
/usr/share/kig/icons/hicolor/32x32/actions/directrix.png
/usr/share/kig/icons/hicolor/32x32/actions/distance.png
/usr/share/kig/icons/hicolor/32x32/actions/ellipsebffp.png
/usr/share/kig/icons/hicolor/32x32/actions/en.png
/usr/share/kig/icons/hicolor/32x32/actions/equilateralhyperbolab4p.png
/usr/share/kig/icons/hicolor/32x32/actions/equitriangle.png
/usr/share/kig/icons/hicolor/32x32/actions/genericaffinity.png
/usr/share/kig/icons/hicolor/32x32/actions/genericprojectivity.png
/usr/share/kig/icons/hicolor/32x32/actions/halflinebyvector.png
/usr/share/kig/icons/hicolor/32x32/actions/harmonichomology.png
/usr/share/kig/icons/hicolor/32x32/actions/hexagonbcv.png
/usr/share/kig/icons/hicolor/32x32/actions/hyperbolabffp.png
/usr/share/kig/icons/hicolor/32x32/actions/intersection.png
/usr/share/kig/icons/hicolor/32x32/actions/inversion.png
/usr/share/kig/icons/hicolor/32x32/actions/kig_numericvalue.png
/usr/share/kig/icons/hicolor/32x32/actions/kig_polygon.png
/usr/share/kig/icons/hicolor/32x32/actions/kig_text.png
/usr/share/kig/icons/hicolor/32x32/actions/line.png
/usr/share/kig/icons/hicolor/32x32/actions/linebyvector.png
/usr/share/kig/icons/hicolor/32x32/actions/locus.png
/usr/share/kig/icons/hicolor/32x32/actions/mirrorpoint.png
/usr/share/kig/icons/hicolor/32x32/actions/openpolygon.png
/usr/share/kig/icons/hicolor/32x32/actions/paint.png
/usr/share/kig/icons/hicolor/32x32/actions/parabolabtp.png
/usr/share/kig/icons/hicolor/32x32/actions/parallel.png
/usr/share/kig/icons/hicolor/32x32/actions/perpendicular.png
/usr/share/kig/icons/hicolor/32x32/actions/point.png
/usr/share/kig/icons/hicolor/32x32/actions/pointOnLine.png
/usr/share/kig/icons/hicolor/32x32/actions/pointxy.png
/usr/share/kig/icons/hicolor/32x32/actions/polygonsides.png
/usr/share/kig/icons/hicolor/32x32/actions/polygonvertices.png
/usr/share/kig/icons/hicolor/32x32/actions/projection.png
/usr/share/kig/icons/hicolor/32x32/actions/python.png
/usr/share/kig/icons/hicolor/32x32/actions/radicalline.png
/usr/share/kig/icons/hicolor/32x32/actions/ray.png
/usr/share/kig/icons/hicolor/32x32/actions/rbezier3.png
/usr/share/kig/icons/hicolor/32x32/actions/rbezier4.png
/usr/share/kig/icons/hicolor/32x32/actions/rbezierN.png
/usr/share/kig/icons/hicolor/32x32/actions/rotation.png
/usr/share/kig/icons/hicolor/32x32/actions/scale.png
/usr/share/kig/icons/hicolor/32x32/actions/segment.png
/usr/share/kig/icons/hicolor/32x32/actions/segment_golden_point.png
/usr/share/kig/icons/hicolor/32x32/actions/segment_midpoint.png
/usr/share/kig/icons/hicolor/32x32/actions/segmentaxis.png
/usr/share/kig/icons/hicolor/32x32/actions/similitude.png
/usr/share/kig/icons/hicolor/32x32/actions/sizer.png
/usr/share/kig/icons/hicolor/32x32/actions/slope.png
/usr/share/kig/icons/hicolor/32x32/actions/square.png
/usr/share/kig/icons/hicolor/32x32/actions/stretch.png
/usr/share/kig/icons/hicolor/32x32/actions/tangent.png
/usr/share/kig/icons/hicolor/32x32/actions/test.png
/usr/share/kig/icons/hicolor/32x32/actions/testcollinear.png
/usr/share/kig/icons/hicolor/32x32/actions/testcontains.png
/usr/share/kig/icons/hicolor/32x32/actions/testdistance.png
/usr/share/kig/icons/hicolor/32x32/actions/testorthogonal.png
/usr/share/kig/icons/hicolor/32x32/actions/testparallel.png
/usr/share/kig/icons/hicolor/32x32/actions/translation.png
/usr/share/kig/icons/hicolor/32x32/actions/triangle.png
/usr/share/kig/icons/hicolor/32x32/actions/vector.png
/usr/share/kig/icons/hicolor/32x32/actions/vectordifference.png
/usr/share/kig/icons/hicolor/32x32/actions/vectorsum.png
/usr/share/kig/icons/hicolor/32x32/actions/w.png
/usr/share/kig/icons/hicolor/scalable/actions/angle.svgz
/usr/share/kig/icons/hicolor/scalable/actions/angle_bisector.svgz
/usr/share/kig/icons/hicolor/scalable/actions/angle_size.svgz
/usr/share/kig/icons/hicolor/scalable/actions/arc.svgz
/usr/share/kig/icons/hicolor/scalable/actions/arc_center.svgz
/usr/share/kig/icons/hicolor/scalable/actions/areaCircle.svgz
/usr/share/kig/icons/hicolor/scalable/actions/attacher.svgz
/usr/share/kig/icons/hicolor/scalable/actions/baseCircle.svgz
/usr/share/kig/icons/hicolor/scalable/actions/bezier3.svgz
/usr/share/kig/icons/hicolor/scalable/actions/bezier4.svgz
/usr/share/kig/icons/hicolor/scalable/actions/bezierN.svgz
/usr/share/kig/icons/hicolor/scalable/actions/beziercurves.svgz
/usr/share/kig/icons/hicolor/scalable/actions/bisection.svgz
/usr/share/kig/icons/hicolor/scalable/actions/centerofcurvature.svgz
/usr/share/kig/icons/hicolor/scalable/actions/centralsymmetry.svgz
/usr/share/kig/icons/hicolor/scalable/actions/circlebcl.svgz
/usr/share/kig/icons/hicolor/scalable/actions/circlebcp.svgz
/usr/share/kig/icons/hicolor/scalable/actions/circlebpd.svgz
/usr/share/kig/icons/hicolor/scalable/actions/circlebps.svgz
/usr/share/kig/icons/hicolor/scalable/actions/circlebtp.svgz
/usr/share/kig/icons/hicolor/scalable/actions/circlelineintersection.svgz
/usr/share/kig/icons/hicolor/scalable/actions/circumference.svgz
/usr/share/kig/icons/hicolor/scalable/actions/conicasymptotes.svgz
/usr/share/kig/icons/hicolor/scalable/actions/conicb5p.svgz
/usr/share/kig/icons/hicolor/scalable/actions/coniclineintersection.svgz
/usr/share/kig/icons/hicolor/scalable/actions/conicsradicalline.svgz
/usr/share/kig/icons/hicolor/scalable/actions/controlpolygon.svgz
/usr/share/kig/icons/hicolor/scalable/actions/convexhull.svgz
/usr/share/kig/icons/hicolor/scalable/actions/curvelineintersection.svgz
/usr/share/kig/icons/hicolor/scalable/actions/directrix.svgz
/usr/share/kig/icons/hicolor/scalable/actions/distance.svgz
/usr/share/kig/icons/hicolor/scalable/actions/ellipsebffp.svgz
/usr/share/kig/icons/hicolor/scalable/actions/en.svgz
/usr/share/kig/icons/hicolor/scalable/actions/equilateralhyperbolab4p.svgz
/usr/share/kig/icons/hicolor/scalable/actions/equitriangle.svgz
/usr/share/kig/icons/hicolor/scalable/actions/genericaffinity.svgz
/usr/share/kig/icons/hicolor/scalable/actions/genericprojectivity.svgz
/usr/share/kig/icons/hicolor/scalable/actions/halflinebyvector.svgz
/usr/share/kig/icons/hicolor/scalable/actions/harmonichomology.svgz
/usr/share/kig/icons/hicolor/scalable/actions/hexagonbcv.svgz
/usr/share/kig/icons/hicolor/scalable/actions/hyperbolabffp.svgz
/usr/share/kig/icons/hicolor/scalable/actions/intersection.svgz
/usr/share/kig/icons/hicolor/scalable/actions/inversion.svgz
/usr/share/kig/icons/hicolor/scalable/actions/kig_numericvalue.svgz
/usr/share/kig/icons/hicolor/scalable/actions/kig_polygon.svgz
/usr/share/kig/icons/hicolor/scalable/actions/kig_text.svgz
/usr/share/kig/icons/hicolor/scalable/actions/line.svgz
/usr/share/kig/icons/hicolor/scalable/actions/linebyvector.svgz
/usr/share/kig/icons/hicolor/scalable/actions/locus.svgz
/usr/share/kig/icons/hicolor/scalable/actions/mirrorpoint.svgz
/usr/share/kig/icons/hicolor/scalable/actions/openpolygon.svgz
/usr/share/kig/icons/hicolor/scalable/actions/paint.svgz
/usr/share/kig/icons/hicolor/scalable/actions/parabolabtp.svgz
/usr/share/kig/icons/hicolor/scalable/actions/parallel.svgz
/usr/share/kig/icons/hicolor/scalable/actions/perpendicular.svgz
/usr/share/kig/icons/hicolor/scalable/actions/point.svgz
/usr/share/kig/icons/hicolor/scalable/actions/pointOnLine.svgz
/usr/share/kig/icons/hicolor/scalable/actions/pointxy.svgz
/usr/share/kig/icons/hicolor/scalable/actions/polygonsides.svgz
/usr/share/kig/icons/hicolor/scalable/actions/polygonvertices.svgz
/usr/share/kig/icons/hicolor/scalable/actions/projection.svgz
/usr/share/kig/icons/hicolor/scalable/actions/python.svgz
/usr/share/kig/icons/hicolor/scalable/actions/radicalline.svgz
/usr/share/kig/icons/hicolor/scalable/actions/ray.svgz
/usr/share/kig/icons/hicolor/scalable/actions/rbezier3.svgz
/usr/share/kig/icons/hicolor/scalable/actions/rbezier4.svgz
/usr/share/kig/icons/hicolor/scalable/actions/rbezierN.svgz
/usr/share/kig/icons/hicolor/scalable/actions/rotation.svgz
/usr/share/kig/icons/hicolor/scalable/actions/scale.svgz
/usr/share/kig/icons/hicolor/scalable/actions/segment.svgz
/usr/share/kig/icons/hicolor/scalable/actions/segment_golden_point.svgz
/usr/share/kig/icons/hicolor/scalable/actions/segment_midpoint.svgz
/usr/share/kig/icons/hicolor/scalable/actions/segmentaxis.svgz
/usr/share/kig/icons/hicolor/scalable/actions/similitude.svgz
/usr/share/kig/icons/hicolor/scalable/actions/sizer.svgz
/usr/share/kig/icons/hicolor/scalable/actions/slope.svgz
/usr/share/kig/icons/hicolor/scalable/actions/square.svgz
/usr/share/kig/icons/hicolor/scalable/actions/stretch.svgz
/usr/share/kig/icons/hicolor/scalable/actions/tangent.svgz
/usr/share/kig/icons/hicolor/scalable/actions/test.svgz
/usr/share/kig/icons/hicolor/scalable/actions/testcollinear.svgz
/usr/share/kig/icons/hicolor/scalable/actions/testcontains.svgz
/usr/share/kig/icons/hicolor/scalable/actions/testdistance.svgz
/usr/share/kig/icons/hicolor/scalable/actions/testorthogonal.svgz
/usr/share/kig/icons/hicolor/scalable/actions/testparallel.svgz
/usr/share/kig/icons/hicolor/scalable/actions/translation.svgz
/usr/share/kig/icons/hicolor/scalable/actions/triangle.svgz
/usr/share/kig/icons/hicolor/scalable/actions/vector.svgz
/usr/share/kig/icons/hicolor/scalable/actions/vectordifference.svgz
/usr/share/kig/icons/hicolor/scalable/actions/vectorsum.svgz
/usr/share/kig/icons/hicolor/scalable/actions/w.svgz
/usr/share/kig/tips
/usr/share/kservices5/kig_part.desktop
/usr/share/kxmlgui5/kig/kigpartui.rc
/usr/share/kxmlgui5/kig/kigui.rc
/usr/share/metainfo/org.kde.kig.appdata.xml

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/kig/index.cache.bz2
/usr/share/doc/HTML/ca/kig/index.docbook
/usr/share/doc/HTML/de/kig/constructed_a_point.png
/usr/share/doc/HTML/de/kig/constructed_script_object.png
/usr/share/doc/HTML/de/kig/constructing_a_circle.png
/usr/share/doc/HTML/de/kig/constructing_a_circle_2.png
/usr/share/doc/HTML/de/kig/edit_types_dialog.png
/usr/share/doc/HTML/de/kig/index.cache.bz2
/usr/share/doc/HTML/de/kig/index.docbook
/usr/share/doc/HTML/de/kig/macro_wizard.png
/usr/share/doc/HTML/de/kig/macros_at_work.png
/usr/share/doc/HTML/de/kig/script_wizard.png
/usr/share/doc/HTML/de/kig/script_wizard_entering_code.png
/usr/share/doc/HTML/de/kig/selecting_objects.png
/usr/share/doc/HTML/de/kig/simple_locus_construction.png
/usr/share/doc/HTML/de/kig/test_run_macro.png
/usr/share/doc/HTML/de/kig/text_label_attaching.png
/usr/share/doc/HTML/de/kig/text_label_wizard.png
/usr/share/doc/HTML/de/kig/text_label_wizard__select_property.png
/usr/share/doc/HTML/en/kig/constructed_a_point.png
/usr/share/doc/HTML/en/kig/constructed_script_object.png
/usr/share/doc/HTML/en/kig/constructing_a_circle.png
/usr/share/doc/HTML/en/kig/constructing_a_circle_2.png
/usr/share/doc/HTML/en/kig/edit_types_dialog.png
/usr/share/doc/HTML/en/kig/index.cache.bz2
/usr/share/doc/HTML/en/kig/index.docbook
/usr/share/doc/HTML/en/kig/macro_wizard.png
/usr/share/doc/HTML/en/kig/macros_at_work.png
/usr/share/doc/HTML/en/kig/script_wizard.png
/usr/share/doc/HTML/en/kig/script_wizard_entering_code.png
/usr/share/doc/HTML/en/kig/selecting_objects.png
/usr/share/doc/HTML/en/kig/simple_locus_construction.png
/usr/share/doc/HTML/en/kig/test_run_macro.png
/usr/share/doc/HTML/en/kig/text_label_attaching.png
/usr/share/doc/HTML/en/kig/text_label_wizard.png
/usr/share/doc/HTML/en/kig/text_label_wizard__select_property.png
/usr/share/doc/HTML/es/kig/index.cache.bz2
/usr/share/doc/HTML/es/kig/index.docbook
/usr/share/doc/HTML/et/kig/index.cache.bz2
/usr/share/doc/HTML/et/kig/index.docbook
/usr/share/doc/HTML/it/kig/index.cache.bz2
/usr/share/doc/HTML/it/kig/index.docbook
/usr/share/doc/HTML/nl/kig/index.cache.bz2
/usr/share/doc/HTML/nl/kig/index.docbook
/usr/share/doc/HTML/pt_BR/kig/index.cache.bz2
/usr/share/doc/HTML/pt_BR/kig/index.docbook
/usr/share/doc/HTML/sv/kig/index.cache.bz2
/usr/share/doc/HTML/sv/kig/index.docbook
/usr/share/doc/HTML/uk/kig/constructed_a_point.png
/usr/share/doc/HTML/uk/kig/constructed_script_object.png
/usr/share/doc/HTML/uk/kig/constructing_a_circle.png
/usr/share/doc/HTML/uk/kig/constructing_a_circle_2.png
/usr/share/doc/HTML/uk/kig/edit_types_dialog.png
/usr/share/doc/HTML/uk/kig/index.cache.bz2
/usr/share/doc/HTML/uk/kig/index.docbook
/usr/share/doc/HTML/uk/kig/macro_wizard.png
/usr/share/doc/HTML/uk/kig/macros_at_work.png
/usr/share/doc/HTML/uk/kig/script_wizard.png
/usr/share/doc/HTML/uk/kig/script_wizard_entering_code.png
/usr/share/doc/HTML/uk/kig/selecting_objects.png
/usr/share/doc/HTML/uk/kig/simple_locus_construction.png
/usr/share/doc/HTML/uk/kig/test_run_macro.png
/usr/share/doc/HTML/uk/kig/text_label_attaching.png
/usr/share/doc/HTML/uk/kig/text_label_wizard.png
/usr/share/doc/HTML/uk/kig/text_label_wizard__select_property.png

%files lib
%defattr(-,root,root,-)
/usr/lib64/qt5/plugins/kigpart.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kig/COPYING
/usr/share/package-licenses/kig/COPYING.DOC
/usr/share/package-licenses/kig/cmake_modules_COPYING-CMAKE-SCRIPTS

%files man
%defattr(0644,root,root,0755)
/usr/share/man/ca/man1/kig.1
/usr/share/man/de/man1/kig.1
/usr/share/man/es/man1/kig.1
/usr/share/man/et/man1/kig.1
/usr/share/man/it/man1/kig.1
/usr/share/man/man1/kig.1
/usr/share/man/nl/man1/kig.1
/usr/share/man/pt_BR/man1/kig.1
/usr/share/man/ru/man1/kig.1
/usr/share/man/sv/man1/kig.1
/usr/share/man/uk/man1/kig.1

%files locales -f kfile_drgeo.lang -f kfile_kig.lang -f kig.lang
%defattr(-,root,root,-)

