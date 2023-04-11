load("@python_deps//:requirements.bzl", "requirement")
# install_deps()
py_binary(
    name = "main",
    deps = [
            "//projects/calculator:calculator",
            requirement("Flask")
    ],
    srcs = ["main.py"],
)