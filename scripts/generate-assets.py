#!/usr/bin/env python3
"""
Viora アセット生成スクリプト
- assets/icon.png      : X プロフィール用（400×400）
- assets/ogp.png       : OGP 画像（1200×630）

使い方:
  uv run --with cairosvg --with pillow scripts/generate-assets.py
"""

import io
from pathlib import Path

import cairosvg
from PIL import Image, ImageDraw, ImageFont

# ── パス設定 ────────────────────────────────────────────
BASE = Path(__file__).parent.parent
SVG_PATH = BASE / "assets" / "logo.svg"
OUT_ICON = BASE / "assets" / "icon.png"
OUT_OGP  = BASE / "assets" / "ogp.png"

# ── カラー ──────────────────────────────────────────────
BG      = (13, 11, 16)        # #0d0b10
PINK_LT = (240, 208, 220)     # #f0d0dc
MUTED   = (138, 128, 152)     # #8a8098


def svg_to_image(svg_path: Path, size: int) -> Image.Image:
    """SVG を正方形 PNG に変換"""
    png_bytes = cairosvg.svg2png(
        url=str(svg_path),
        output_width=size,
        output_height=size,
    )
    return Image.open(io.BytesIO(png_bytes)).convert("RGBA")


def make_icon(size: int = 400) -> None:
    """X プロフィール用アイコン（正方形）"""
    canvas = Image.new("RGBA", (size, size), BG + (255,))
    symbol = svg_to_image(SVG_PATH, int(size * 0.65))

    # 中央配置
    x = (size - symbol.width) // 2
    y = (size - symbol.height) // 2
    canvas.paste(symbol, (x, y), symbol)

    canvas.convert("RGB").save(OUT_ICON, "PNG", optimize=True)
    print(f"✓ icon.png  ({size}×{size})")


def make_ogp(w: int = 1200, h: int = 630) -> None:
    """OGP 画像（1200×630）"""
    canvas = Image.new("RGB", (w, h), BG)
    draw = ImageDraw.Draw(canvas)

    # ── シンボル（左寄り中央）──
    sym_size = 260
    symbol = svg_to_image(SVG_PATH, sym_size)
    sym_x = w // 2 - sym_size // 2
    sym_y = h // 2 - sym_size // 2 - 30
    canvas.paste(symbol, (sym_x, sym_y), symbol)

    # ── テキスト ──
    try:
        # システムフォントを探す（なければデフォルト）
        font_wordmark = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 72)
        font_sub      = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 32)
    except OSError:
        font_wordmark = ImageFont.load_default()
        font_sub      = ImageFont.load_default()

    # VIORA
    text_viora = "VIORA"
    bbox = draw.textbbox((0, 0), text_viora, font=font_wordmark)
    tw = bbox[2] - bbox[0]
    draw.text(((w - tw) // 2, sym_y + sym_size + 16), text_viora, font=font_wordmark, fill=PINK_LT)

    # Platform for VLiver
    text_sub = "Platform for VLiver"
    bbox2 = draw.textbbox((0, 0), text_sub, font=font_sub)
    tw2 = bbox2[2] - bbox2[0]
    draw.text(((w - tw2) // 2, sym_y + sym_size + 100), text_sub, font=font_sub, fill=MUTED)

    canvas.save(OUT_OGP, "PNG", optimize=True)
    print(f"✓ ogp.png   ({w}×{h})")


if __name__ == "__main__":
    make_icon()
    make_ogp()
    print("完了")
