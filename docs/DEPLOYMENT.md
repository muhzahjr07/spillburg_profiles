# Deployment & Publishing Guide

This guide details how to build, render, test, and deploy the Spillburg Group corporate profiles suite across web, PDF print, Figma, and GitHub Pages.

---

## 1. Automated GitHub Pages Deployment

The repository includes a GitHub Actions workflow (`.github/workflows/deploy-pages.yml`) that automatically deploys the interactive showcase portal and HTML templates whenever changes are pushed to `main`.

### Enabling GitHub Pages in Repository Settings:
1. Navigate to **Settings** > **Pages** in the `muhzahjr07/spillburg_profiles` repository.
2. Under **Build and deployment** > **Source**, select **GitHub Actions**.
3. Every push to `main` will trigger the deployment, and your live portal will be available at:
   ```
   https://muhzahjr07.github.io/spillburg_profiles/docs/
   ```

---

## 2. Rendering High-Resolution PDFs

Master PDFs are rendered via headless Chromium using exact 1920×1080 (16:9) print-emulation styling with 0 margins, guaranteed page breaks, and embedded vector graphics.

```bash
# Execute master PDF rendering and page splitting
python scratch/render_all_three.py
```

This compiles:
- `Company Profile - 2026.pdf` (9-page master presentation/print document)
- `individual_pages/Page 01.pdf` through `Page 09.pdf` (standalone page files)

---

## 3. Exporting Figma Vector SVGs

Vector SVG assets allow direct drag-and-drop into Figma with 100% preservation of typography layers, curves, brand colors, and embedded assets.

```bash
# Export all 9 pages per company into figma_svg_pages/
python scratch/export_all_svgs.py
```

Import instructions:
1. Open any Figma document.
2. Drag and drop any `Page 0X.svg` file from `figma_svg_pages/` into the canvas.
3. Figma automatically recognizes the vector frame and creates editable layers.

---

## 4. Re-compiling Editable PowerPoint Decks

To regenerate the 9-slide PowerPoint presentation decks (`.pptx`):

```bash
python scratch/update_all_pptx.py
```

