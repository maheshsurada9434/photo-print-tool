# Photo Print Sheet Maker

Put passport, stamp, PAN and visa photos of different people on one print-ready sheet, in your browser.

**Open the tool:** https://maheshsurada9434.github.io/photo-print-tool/

![Photo Print Sheet Maker with three photos in the queue and an A4 sheet in the preview](docs/screenshot.jpg)

## What it does

**Print sheets**
- **Queue many photos at once.** Drag and drop, paste from the clipboard, or pick several JPG/PNG files.
- **A size for each photo.** 5-Pic Passport (3.5 × 4.5 cm), 6-Pic Passport (3.2 × 4.1 cm), Stamp (2 × 2.5 cm), Voter / PAN (2.5 × 3.5 cm), US Visa / OCI (2 × 2 inch), UK / Schengen visa, Canada visa (5 × 7 cm), China visa (3.3 × 4.8 cm), signature box, thumb impression, ID / PVC card, or your own size in cm or inches.
- **Copies** with − and +, and **Fill empty space** to top up the last page so no paper is wasted.
- **Ready layouts**: one tap for 8 passport photos on 4×6, 30 or 36 on A4, 90 stamp photos on A4, 12 PAN size on 4×6 or 6 US visa on 4×6.
- **Paper sizes**: A4, A5, 4×6 inch, 5×7 inch, Letter and Legal, in portrait or landscape. Photos of different sizes share the sheet and extra photos flow onto more pages.
- **Margins, gaps, cut lines and a thin white or black border** around each photo.
- **Print or download** a 300 DPI PDF, or download any single photo.

**Fixing the photo**
- **AI background change.** Cuts the person out of any background and puts white, light blue, sky blue, light grey or red behind them. It runs on your device with Google's free MediaPipe model (about 10 MB, downloaded once). A simpler plain-wall method works offline.
- **Auto-fit face.** Finds the face and frames it the passport way; one button does every photo in the queue.
- **Touch-up.** Move, zoom, rotate, straighten, brightness, contrast, colour and one-tap auto-enhance.
- **Name & DOB** strip at the bottom of every copy.

**Exam form photo & signature resizer**
- Makes a photo or signature fit an online form's rules in pixels and KB, for example 200 × 230 px and 20–50 KB for a photo, or 140 × 60 px and 10–20 KB for a signature. Presets cover common bank and SSC style rules, or type your own. Always check your exam notice.
- Signatures can be cleaned to dark ink on a white background.

**Everyday use**
- **Your work is kept.** The queue is saved in this browser, so a refresh or an accidental close does not lose it.
- **Install as an app** on a phone or a shop computer; it opens full screen and keeps working offline after the first visit.

## Printing at the right size

Print at **100% / Actual size**, not *Fit to page*. The PDF pages are exactly the paper size, so a 3.5 × 4.5 cm photo prints at 3.5 × 4.5 cm.

## Privacy

Everything happens in your browser. Photos are never uploaded: the queue is saved only in this browser on this device, and the AI models run on the device too. Use **Clear queue** to remove everything.

## Run it yourself

It is a single `index.html` with no build step and no dependencies. Open it in a browser, or host the folder on GitHub Pages: **Settings → Pages → Deploy from a branch → `main` / root**.

## Credits

Made by **[Mahesh Surada](https://github.com/maheshsurada9434)**.

Background cut-out and face finding use [MediaPipe](https://ai.google.dev/edge/mediapipe) by Google (Apache 2.0), loaded only when you use those features.
