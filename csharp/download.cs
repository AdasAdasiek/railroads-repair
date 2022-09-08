using (var client = new WebClient())
{
    client.DownloadFile("https://github.com/AdasAdasiek/railroads-repair/releases/download/release/RailRoads.exe", "RailRoads.exe");
}
