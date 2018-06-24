from nxtools import NxConanFile
from conans import tools, CMake


class FnvConan(NxConanFile):
    name = "fnv"
    version = "5.0.3"
    url = "http://www.isthe.com/chongo/tech/comp/fnv"
    settings = "os", "compiler", "build_type", "arch"
    description = "Fast and simple non-cryptographic hash algorithm."
    exports_sources = ['CMakeLists.txt']

    def do_source(self):
        self.retrieve("a947995b6606dc91eca79e55fb87f22edce5e5b358a521a7115b18dfc7ab7715",
                [
                    "vendor://fnv/fnv/fnv-{v}.tar.gz".format(v=self.version),
                    "http://www.isthe.com/chongo/src/fnv/fnv-{v}.tar.gz".format(v=self.version)
                ], "fnv-{v}.tar.gz".format(v=self.version))

    def do_build(self):
        cmake = CMake(self)
        tools.untargz("fnv-{v}.tar.gz".format(v=self.version))
        cmake.configure()
        cmake.build(target="install")

    def do_package_info(self):
        self.cpp_info.libs = ["fnv"]

