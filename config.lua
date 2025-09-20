
local configs = {
  LED = "/media/felipe_palagio/BAKITUP",
  DVC = "/dev/sdb1",
  USE = true,
}

-- if run with argument "bash", print as KEY=VALUE
if arg and arg[1] == "bash" then
  for k, v in pairs(configs) do
    if type(v) == "boolean" then
      v = tostring(v):lower()
    end
    print(string.format("%s=%s", k, v))
  end
  os.exit()
end

-- otherwise return for Python
return configs

