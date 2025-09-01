
local configs = {
    LED = "MEDIA FUCKING PATH",
}

for k, v in pairs(configs) do
    if type(v) == "boolean" then
        v = tostring(v):lower()
    end
    print(string.format("%s=%s", k, v))
end
