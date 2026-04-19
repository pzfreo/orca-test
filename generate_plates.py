from pathlib import Path

import cadquery as cq

SIDE_MM = 20.0
THICKNESSES_MM = [4.5, 5.0, 5.5, 6.0]
OUTPUT_DIR = Path("build")


def make_plate(thickness_mm: float) -> cq.Workplane:
    return cq.Workplane("XY").box(SIDE_MM, SIDE_MM, thickness_mm)


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    for thickness in THICKNESSES_MM:
        plate = make_plate(thickness)
        name = f"plate_{SIDE_MM:g}x{SIDE_MM:g}x{thickness:g}mm.step"
        out_path = OUTPUT_DIR / name
        cq.exporters.export(plate, str(out_path))
        print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
