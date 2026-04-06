open("C:/Users/juell/OneDrive/Documents/CM515 Course/Course Work/CM515 GitHub/CM515-2026/modules/wk_10_image_analysis/muscle.tif");
selectImage("muscle.tif");
run("Duplicate...", " ");
selectImage("muscle.tif");
selectImage("muscle-1.tif");
run("Color Threshold...");
run("Split Channels");
run("Fire");
