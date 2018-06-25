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
        self.retrieve("9c52f7189174a471f757adcf8f92c19280bc1fe94bd07bda13b0006287c1a814",
                [
                    "vendor://fnv/fnv/fnv-{v}.tar.gz".format(v=self.version),
                    "http://www.isthe.com/chongo/src/fnv/fnv-{v}.tar.gz".format(v=self.version)
                ], "fnv-{v}.tar".format(v=self.version))

    def do_build(self):
        cmake = CMake(self)
        tools.unzip("fnv-{v}.tar".format(v=self.version))
        cmake.configure()
        cmake.build(target="install")

    def do_package_info(self):
        self.cpp_info.libs = ["fnv"]

