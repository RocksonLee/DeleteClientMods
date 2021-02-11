import os
import glob

client_mods = ["soundsystemreloader", "FpsReducer", "jeivillagers", "dynamistics", "JustEnoughReactors",
               "just-enough-harvestcraft", "gendustryjei", "tinkersjei", "jeiintegration", "fluidict",
               "jeibees", "just-enough-brewcraft", "jepb", "jetif", "ThaumicJEI", "JustEnoughEnergistics",
               "tc6aspects4jei", "JustEnoughResources", "JEROreIntegration", "modnametooltip", "Toast Control",
               "InventoryHud", "FullscreenWindowed", "InvMove", "lootcapacitortooltips", "DynamicSurroundings",
               "DynamicSurroundingsHuds", "AmbientSounds", "MoBends", "BetterFps", "Controlling", "BetterAdvancements",
               "WorldSelectionAdvanced", "BetterFoliage", "lesslag", "TieredTooltips", "ColouredTooltips", "Unifine",
               "ShoulderSurfing", "LoadingScreens", "Tips", "ScreenshotToClipboard", "SplashAnimation",
               "shutupmodelloader", "NonUpdate", "classicbar", "ClientTweaks", "shapeselector", "OldJavaWarning",
               "particleculling", "CTM-MC", "ChatCopier", "WHAT", "ikwid", "SmoothFont", "itlt", "clearwater",
               "StuffASockInIt", "EntityCulling", "MouseTweaks", "JustEnoughCharacters", "MAGE", "MineMenu",
               "BetterPlacement", "ChatFlow", "potiondescriptions", "hiddenarmor", "InGameInfoXML", "memorycleaner",
               "InGameAccountSwitcher", "RealFirstPerson2", "ProportionalDestructionParticles", "PackModeMenu",
               "Modpack Configuration Checker", "MenuMobs", "MainMenuScale", "ResourceLoader", "scalingguis",
               "CustomLoadingScreen", "CustomBackgrounds", "CustomSkinLoader_Forge", "CustomMainMenu", "Blur",
               "InvMove"]

count = 0

for cmodIndex in range(len(client_mods)):
    cmodString = client_mods[cmodIndex] + '*.jar'
    filesFound = glob.glob(cmodString)

    if len(filesFound) >= 1:
        os.remove(filesFound[0])
        print("Deleted " + cmodString)
        count += 1
    else:
        print("Did not find " + cmodString)
print("Finished deleting client mods. Deleted " + str(count) + " mods!")
