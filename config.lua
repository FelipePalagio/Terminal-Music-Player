--AQUI VAI O NOME DO ARMZ EXTERNO
local configs = {
  LED = "/caminho/para/HDDEXT", --EXMPLO
  DVC = "/dev/sdb1", --EXEMPLO 
  USE = true,
}


if arg and arg[1] == "bash" then
  for k, v in pairs(configs) do
    if type(v) == "boolean" then
      v = tostring(v):lower()
    end
    print(string.format("%s=%s", k, v))
  end
  os.exit()
end

return configs

