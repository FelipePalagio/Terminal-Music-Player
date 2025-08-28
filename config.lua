
local configs = {
    LED = "/media/felipe_palagio/BAKITUP",
}

for k, v in pairs(configs) do
    if type(v) == "boolean" then
        v = tostring(v):lower()
    end
    print(string.format("%s=%s", k, v))
end
