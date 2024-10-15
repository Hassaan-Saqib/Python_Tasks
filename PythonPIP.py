#pip --version
#pip install camelcase
import camelcase

c = camelcase.CamelCase()

txt = "hello world"

print(c.hump(txt))

#remove Pip uninstall camelcase
#pip list