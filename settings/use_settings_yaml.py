import yaml
f = open("settings.yaml")
settings = yaml.load(f)

print settings['fps'] + 3 
print settings['float_example']
