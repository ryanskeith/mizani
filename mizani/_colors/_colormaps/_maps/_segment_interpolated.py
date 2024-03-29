from __future__ import annotations

from typing import TYPE_CHECKING

from mizani._colors import ColorMapKind as cmk
from mizani._colors import SegmentInterpolatedMap

if TYPE_CHECKING:
    from mizani.typing import (
        SegmentedColorMapData,
    )

__all__ = (
    # sequential
    "Wistia",
    "autumn",
    "binary",
    "bone",
    "cool",
    "copper",
    "gray",
    "hot",
    "pink",
    "spring",
    "summer",
    "winter",
    # diverging
    "coolwarm",
    # miscalleneous
    "CMRmap",
    "gist_earth",
    "gist_ncar",
    "gist_stern",
    "jet",
    "nipy_spectral",
)

# sequential
_autumn: SegmentedColorMapData = {
    "blue": ((0.0, 0.0, 0.0), (1.0, 0.0, 0.0)),
    "green": ((0.0, 0.0, 0.0), (1.0, 1.0, 1.0)),
    "red": ((0.0, 1.0, 1.0), (1.0, 1.0, 1.0)),
}


_binary: SegmentedColorMapData = {
    "blue": ((0.0, 1.0, 1.0), (1.0, 0.0, 0.0)),
    "green": ((0.0, 1.0, 1.0), (1.0, 0.0, 0.0)),
    "red": ((0.0, 1.0, 1.0), (1.0, 0.0, 0.0)),
}


_bone: SegmentedColorMapData = {
    "blue": ((0.0, 0.0, 0.0), (0.365079, 0.444444, 0.444444), (1.0, 1.0, 1.0)),
    "green": (
        (0.0, 0.0, 0.0),
        (0.365079, 0.319444, 0.319444),
        (0.746032, 0.777778, 0.777778),
        (1.0, 1.0, 1.0),
    ),
    "red": ((0.0, 0.0, 0.0), (0.746032, 0.652778, 0.652778), (1.0, 1.0, 1.0)),
}


_cool: SegmentedColorMapData = {
    "blue": ((0.0, 1.0, 1.0), (1.0, 1.0, 1.0)),
    "green": ((0.0, 1.0, 1.0), (1.0, 0.0, 0.0)),
    "red": ((0.0, 0.0, 0.0), (1.0, 1.0, 1.0)),
}


_copper: SegmentedColorMapData = {
    "blue": ((0.0, 0.0, 0.0), (1.0, 0.4975, 0.4975)),
    "green": ((0.0, 0.0, 0.0), (1.0, 0.7812, 0.7812)),
    "red": ((0.0, 0.0, 0.0), (0.809524, 1.0, 1.0), (1.0, 1.0, 1.0)),
}


_gray: SegmentedColorMapData = {
    "blue": ((0.0, 0, 0), (1.0, 1, 1)),
    "green": ((0.0, 0, 0), (1.0, 1, 1)),
    "red": ((0.0, 0, 0), (1.0, 1, 1)),
}


_hot: SegmentedColorMapData = {
    "blue": ((0.0, 0.0, 0.0), (0.746032, 0.0, 0.0), (1.0, 1.0, 1.0)),
    "green": (
        (0.0, 0.0, 0.0),
        (0.365079, 0.0, 0.0),
        (0.746032, 1.0, 1.0),
        (1.0, 1.0, 1.0),
    ),
    "red": ((0.0, 0.0416, 0.0416), (0.365079, 1.0, 1.0), (1.0, 1.0, 1.0)),
}

_pink: SegmentedColorMapData = {
    "blue": (
        (0.0, 0.0, 0.0),
        (0.015873, 0.102869, 0.102869),
        (0.031746, 0.145479, 0.145479),
        (0.047619, 0.178174, 0.178174),
        (0.063492, 0.205738, 0.205738),
        (0.079365, 0.230022, 0.230022),
        (0.095238, 0.251976, 0.251976),
        (0.111111, 0.272166, 0.272166),
        (0.126984, 0.290957, 0.290957),
        (0.142857, 0.308607, 0.308607),
        (0.15873, 0.3253, 0.3253),
        (0.174603, 0.341178, 0.341178),
        (0.190476, 0.356348, 0.356348),
        (0.206349, 0.370899, 0.370899),
        (0.222222, 0.3849, 0.3849),
        (0.238095, 0.39841, 0.39841),
        (0.253968, 0.411476, 0.411476),
        (0.269841, 0.424139, 0.424139),
        (0.285714, 0.436436, 0.436436),
        (0.301587, 0.448395, 0.448395),
        (0.31746, 0.460044, 0.460044),
        (0.333333, 0.471405, 0.471405),
        (0.349206, 0.482498, 0.482498),
        (0.365079, 0.493342, 0.493342),
        (0.380952, 0.503953, 0.503953),
        (0.396825, 0.514344, 0.514344),
        (0.412698, 0.524531, 0.524531),
        (0.428571, 0.534522, 0.534522),
        (0.444444, 0.544331, 0.544331),
        (0.460317, 0.553966, 0.553966),
        (0.47619, 0.563436, 0.563436),
        (0.492063, 0.57275, 0.57275),
        (0.507937, 0.581914, 0.581914),
        (0.52381, 0.590937, 0.590937),
        (0.539683, 0.599824, 0.599824),
        (0.555556, 0.608581, 0.608581),
        (0.571429, 0.617213, 0.617213),
        (0.587302, 0.625727, 0.625727),
        (0.603175, 0.634126, 0.634126),
        (0.619048, 0.642416, 0.642416),
        (0.634921, 0.6506, 0.6506),
        (0.650794, 0.658682, 0.658682),
        (0.666667, 0.666667, 0.666667),
        (0.68254, 0.674556, 0.674556),
        (0.698413, 0.682355, 0.682355),
        (0.714286, 0.690066, 0.690066),
        (0.730159, 0.697691, 0.697691),
        (0.746032, 0.705234, 0.705234),
        (0.761905, 0.727166, 0.727166),
        (0.777778, 0.748455, 0.748455),
        (0.793651, 0.769156, 0.769156),
        (0.809524, 0.789314, 0.789314),
        (0.825397, 0.808969, 0.808969),
        (0.84127, 0.828159, 0.828159),
        (0.857143, 0.846913, 0.846913),
        (0.873016, 0.865261, 0.865261),
        (0.888889, 0.883229, 0.883229),
        (0.904762, 0.900837, 0.900837),
        (0.920635, 0.918109, 0.918109),
        (0.936508, 0.935061, 0.935061),
        (0.952381, 0.951711, 0.951711),
        (0.968254, 0.968075, 0.968075),
        (0.984127, 0.984167, 0.984167),
        (1.0, 1.0, 1.0),
    ),
    "green": (
        (0.0, 0.0, 0.0),
        (0.015873, 0.102869, 0.102869),
        (0.031746, 0.145479, 0.145479),
        (0.047619, 0.178174, 0.178174),
        (0.063492, 0.205738, 0.205738),
        (0.079365, 0.230022, 0.230022),
        (0.095238, 0.251976, 0.251976),
        (0.111111, 0.272166, 0.272166),
        (0.126984, 0.290957, 0.290957),
        (0.142857, 0.308607, 0.308607),
        (0.15873, 0.3253, 0.3253),
        (0.174603, 0.341178, 0.341178),
        (0.190476, 0.356348, 0.356348),
        (0.206349, 0.370899, 0.370899),
        (0.222222, 0.3849, 0.3849),
        (0.238095, 0.39841, 0.39841),
        (0.253968, 0.411476, 0.411476),
        (0.269841, 0.424139, 0.424139),
        (0.285714, 0.436436, 0.436436),
        (0.301587, 0.448395, 0.448395),
        (0.31746, 0.460044, 0.460044),
        (0.333333, 0.471405, 0.471405),
        (0.349206, 0.482498, 0.482498),
        (0.365079, 0.493342, 0.493342),
        (0.380952, 0.517549, 0.517549),
        (0.396825, 0.540674, 0.540674),
        (0.412698, 0.562849, 0.562849),
        (0.428571, 0.584183, 0.584183),
        (0.444444, 0.604765, 0.604765),
        (0.460317, 0.624669, 0.624669),
        (0.47619, 0.643958, 0.643958),
        (0.492063, 0.662687, 0.662687),
        (0.507937, 0.6809, 0.6809),
        (0.52381, 0.698638, 0.698638),
        (0.539683, 0.715937, 0.715937),
        (0.555556, 0.732828, 0.732828),
        (0.571429, 0.749338, 0.749338),
        (0.587302, 0.765493, 0.765493),
        (0.603175, 0.781313, 0.781313),
        (0.619048, 0.796819, 0.796819),
        (0.634921, 0.812029, 0.812029),
        (0.650794, 0.82696, 0.82696),
        (0.666667, 0.841625, 0.841625),
        (0.68254, 0.85604, 0.85604),
        (0.698413, 0.870216, 0.870216),
        (0.714286, 0.884164, 0.884164),
        (0.730159, 0.897896, 0.897896),
        (0.746032, 0.911421, 0.911421),
        (0.761905, 0.917208, 0.917208),
        (0.777778, 0.922958, 0.922958),
        (0.793651, 0.928673, 0.928673),
        (0.809524, 0.934353, 0.934353),
        (0.825397, 0.939999, 0.939999),
        (0.84127, 0.945611, 0.945611),
        (0.857143, 0.95119, 0.95119),
        (0.873016, 0.956736, 0.956736),
        (0.888889, 0.96225, 0.96225),
        (0.904762, 0.967733, 0.967733),
        (0.920635, 0.973185, 0.973185),
        (0.936508, 0.978607, 0.978607),
        (0.952381, 0.983999, 0.983999),
        (0.968254, 0.989361, 0.989361),
        (0.984127, 0.994695, 0.994695),
        (1.0, 1.0, 1.0),
    ),
    "red": (
        (0.0, 0.1178, 0.1178),
        (0.015873, 0.195857, 0.195857),
        (0.031746, 0.250661, 0.250661),
        (0.047619, 0.295468, 0.295468),
        (0.063492, 0.334324, 0.334324),
        (0.079365, 0.369112, 0.369112),
        (0.095238, 0.400892, 0.400892),
        (0.111111, 0.430331, 0.430331),
        (0.126984, 0.457882, 0.457882),
        (0.142857, 0.483867, 0.483867),
        (0.15873, 0.508525, 0.508525),
        (0.174603, 0.532042, 0.532042),
        (0.190476, 0.554563, 0.554563),
        (0.206349, 0.576204, 0.576204),
        (0.222222, 0.597061, 0.597061),
        (0.238095, 0.617213, 0.617213),
        (0.253968, 0.636729, 0.636729),
        (0.269841, 0.655663, 0.655663),
        (0.285714, 0.674066, 0.674066),
        (0.301587, 0.69198, 0.69198),
        (0.31746, 0.709441, 0.709441),
        (0.333333, 0.726483, 0.726483),
        (0.349206, 0.743134, 0.743134),
        (0.365079, 0.759421, 0.759421),
        (0.380952, 0.766356, 0.766356),
        (0.396825, 0.773229, 0.773229),
        (0.412698, 0.780042, 0.780042),
        (0.428571, 0.786796, 0.786796),
        (0.444444, 0.793492, 0.793492),
        (0.460317, 0.800132, 0.800132),
        (0.47619, 0.806718, 0.806718),
        (0.492063, 0.81325, 0.81325),
        (0.507937, 0.81973, 0.81973),
        (0.52381, 0.82616, 0.82616),
        (0.539683, 0.832539, 0.832539),
        (0.555556, 0.83887, 0.83887),
        (0.571429, 0.845154, 0.845154),
        (0.587302, 0.851392, 0.851392),
        (0.603175, 0.857584, 0.857584),
        (0.619048, 0.863731, 0.863731),
        (0.634921, 0.869835, 0.869835),
        (0.650794, 0.875897, 0.875897),
        (0.666667, 0.881917, 0.881917),
        (0.68254, 0.887896, 0.887896),
        (0.698413, 0.893835, 0.893835),
        (0.714286, 0.899735, 0.899735),
        (0.730159, 0.905597, 0.905597),
        (0.746032, 0.911421, 0.911421),
        (0.761905, 0.917208, 0.917208),
        (0.777778, 0.922958, 0.922958),
        (0.793651, 0.928673, 0.928673),
        (0.809524, 0.934353, 0.934353),
        (0.825397, 0.939999, 0.939999),
        (0.84127, 0.945611, 0.945611),
        (0.857143, 0.95119, 0.95119),
        (0.873016, 0.956736, 0.956736),
        (0.888889, 0.96225, 0.96225),
        (0.904762, 0.967733, 0.967733),
        (0.920635, 0.973185, 0.973185),
        (0.936508, 0.978607, 0.978607),
        (0.952381, 0.983999, 0.983999),
        (0.968254, 0.989361, 0.989361),
        (0.984127, 0.994695, 0.994695),
        (1.0, 1.0, 1.0),
    ),
}


_spring: SegmentedColorMapData = {
    "blue": ((0.0, 1.0, 1.0), (1.0, 0.0, 0.0)),
    "green": ((0.0, 0.0, 0.0), (1.0, 1.0, 1.0)),
    "red": ((0.0, 1.0, 1.0), (1.0, 1.0, 1.0)),
}


_summer: SegmentedColorMapData = {
    "blue": ((0.0, 0.4, 0.4), (1.0, 0.4, 0.4)),
    "green": ((0.0, 0.5, 0.5), (1.0, 1.0, 1.0)),
    "red": ((0.0, 0.0, 0.0), (1.0, 1.0, 1.0)),
}


_winter: SegmentedColorMapData = {
    "blue": ((0.0, 1.0, 1.0), (1.0, 0.5, 0.5)),
    "green": ((0.0, 0.0, 0.0), (1.0, 1.0, 1.0)),
    "red": ((0.0, 0.0, 0.0), (1.0, 0.0, 0.0)),
}

_wistia: SegmentedColorMapData = {
    "red": (
        (0.0, 0.8941176470588236, 0.8941176470588236),
        (0.25, 1.0, 1.0),
        (0.5, 1.0, 1.0),
        (0.75, 1.0, 1.0),
        (1.0, 0.9882352941176471, 0.9882352941176471),
    ),
    "green": (
        (0.0, 1.0, 1.0),
        (0.25, 0.9098039215686274, 0.9098039215686274),
        (0.5, 0.7411764705882353, 0.7411764705882353),
        (0.75, 0.6274509803921569, 0.6274509803921569),
        (1.0, 0.4980392156862745, 0.4980392156862745),
    ),
    "blue": (
        (0.0, 0.47843137254901963, 0.47843137254901963),
        (0.25, 0.10196078431372549, 0.10196078431372549),
        (0.5, 0.0, 0.0),
        (0.75, 0.0, 0.0),
        (1.0, 0.0, 0.0),
    ),
}

# diverging

_coolwarm: SegmentedColorMapData = {
    "red": (
        (0.0, 0.2298057, 0.2298057),
        (0.03125, 0.26623388, 0.26623388),
        (0.0625, 0.30386891, 0.30386891),
        (0.09375, 0.342804478, 0.342804478),
        (0.125, 0.38301334, 0.38301334),
        (0.15625, 0.424369608, 0.424369608),
        (0.1875, 0.46666708, 0.46666708),
        (0.21875, 0.509635204, 0.509635204),
        (0.25, 0.552953156, 0.552953156),
        (0.28125, 0.596262162, 0.596262162),
        (0.3125, 0.639176211, 0.639176211),
        (0.34375, 0.681291281, 0.681291281),
        (0.375, 0.722193294, 0.722193294),
        (0.40625, 0.761464949, 0.761464949),
        (0.4375, 0.798691636, 0.798691636),
        (0.46875, 0.833466556, 0.833466556),
        (0.5, 0.865395197, 0.865395197),
        (0.53125, 0.897787179, 0.897787179),
        (0.5625, 0.924127593, 0.924127593),
        (0.59375, 0.944468518, 0.944468518),
        (0.625, 0.958852946, 0.958852946),
        (0.65625, 0.96732803, 0.96732803),
        (0.6875, 0.969954137, 0.969954137),
        (0.71875, 0.966811177, 0.966811177),
        (0.75, 0.958003065, 0.958003065),
        (0.78125, 0.943660866, 0.943660866),
        (0.8125, 0.923944917, 0.923944917),
        (0.84375, 0.89904617, 0.89904617),
        (0.875, 0.869186849, 0.869186849),
        (0.90625, 0.834620542, 0.834620542),
        (0.9375, 0.795631745, 0.795631745),
        (0.96875, 0.752534934, 0.752534934),
        (1.0, 0.705673158, 0.705673158),
    ),
    "green": (
        (0.0, 0.298717966, 0.298717966),
        (0.03125, 0.353094838, 0.353094838),
        (0.0625, 0.406535296, 0.406535296),
        (0.09375, 0.458757618, 0.458757618),
        (0.125, 0.50941904, 0.50941904),
        (0.15625, 0.558148092, 0.558148092),
        (0.1875, 0.604562568, 0.604562568),
        (0.21875, 0.648280772, 0.648280772),
        (0.25, 0.688929332, 0.688929332),
        (0.28125, 0.726149107, 0.726149107),
        (0.3125, 0.759599947, 0.759599947),
        (0.34375, 0.788964712, 0.788964712),
        (0.375, 0.813952739, 0.813952739),
        (0.40625, 0.834302879, 0.834302879),
        (0.4375, 0.849786142, 0.849786142),
        (0.46875, 0.860207984, 0.860207984),
        (0.5, 0.86541021, 0.86541021),
        (0.53125, 0.848937047, 0.848937047),
        (0.5625, 0.827384882, 0.827384882),
        (0.59375, 0.800927443, 0.800927443),
        (0.625, 0.769767752, 0.769767752),
        (0.65625, 0.734132809, 0.734132809),
        (0.6875, 0.694266682, 0.694266682),
        (0.71875, 0.650421156, 0.650421156),
        (0.75, 0.602842431, 0.602842431),
        (0.78125, 0.551750968, 0.551750968),
        (0.8125, 0.49730856, 0.49730856),
        (0.84375, 0.439559467, 0.439559467),
        (0.875, 0.378313092, 0.378313092),
        (0.90625, 0.312874446, 0.312874446),
        (0.9375, 0.24128379, 0.24128379),
        (0.96875, 0.157246067, 0.157246067),
        (1.0, 0.01555616, 0.01555616),
    ),
    "blue": (
        (0.0, 0.753683153, 0.753683153),
        (0.03125, 0.801466763, 0.801466763),
        (0.0625, 0.84495867, 0.84495867),
        (0.09375, 0.883725899, 0.883725899),
        (0.125, 0.917387822, 0.917387822),
        (0.15625, 0.945619588, 0.945619588),
        (0.1875, 0.968154911, 0.968154911),
        (0.21875, 0.98478814, 0.98478814),
        (0.25, 0.995375608, 0.995375608),
        (0.28125, 0.999836203, 0.999836203),
        (0.3125, 0.998151185, 0.998151185),
        (0.34375, 0.990363227, 0.990363227),
        (0.375, 0.976574709, 0.976574709),
        (0.40625, 0.956945269, 0.956945269),
        (0.4375, 0.931688648, 0.931688648),
        (0.46875, 0.901068838, 0.901068838),
        (0.5, 0.865395561, 0.865395561),
        (0.53125, 0.820880546, 0.820880546),
        (0.5625, 0.774508472, 0.774508472),
        (0.59375, 0.726736146, 0.726736146),
        (0.625, 0.678007945, 0.678007945),
        (0.65625, 0.628751763, 0.628751763),
        (0.6875, 0.579375448, 0.579375448),
        (0.71875, 0.530263762, 0.530263762),
        (0.75, 0.481775914, 0.481775914),
        (0.78125, 0.434243684, 0.434243684),
        (0.8125, 0.387970225, 0.387970225),
        (0.84375, 0.343229596, 0.343229596),
        (0.875, 0.300267182, 0.300267182),
        (0.90625, 0.259301199, 0.259301199),
        (0.9375, 0.220525627, 0.220525627),
        (0.96875, 0.184115123, 0.184115123),
        (1.0, 0.150232812, 0.150232812),
    ),
}


# cyclic
_hsv: SegmentedColorMapData = {
    "blue": (
        (0.0, 0.0, 0.0),
        (0.333333, 0.0, 0.0),
        (0.349206, 0.0625, 0.0625),
        (0.507937, 1.0, 1.0),
        (0.84127, 1.0, 1.0),
        (0.857143, 0.9375, 0.9375),
        (1.0, 0.09375, 0.09375),
    ),
    "green": (
        (0.0, 0.0, 0.0),
        (0.15873, 0.9375, 0.9375),
        (0.174603, 1.0, 1.0),
        (0.507937, 1.0, 1.0),
        (0.666667, 0.0625, 0.0625),
        (0.68254, 0.0, 0.0),
        (1.0, 0.0, 0.0),
    ),
    "red": (
        (0.0, 1.0, 1.0),
        (0.15873, 1.0, 1.0),
        (0.174603, 0.96875, 0.96875),
        (0.333333, 0.03125, 0.03125),
        (0.349206, 0.0, 0.0),
        (0.666667, 0.0, 0.0),
        (0.68254, 0.03125, 0.03125),
        (0.84127, 0.96875, 0.96875),
        (0.857143, 1.0, 1.0),
        (1.0, 1.0, 1.0),
    ),
}


# miscellaneous

_CMRmap: SegmentedColorMapData = {
    "blue": (
        (0.0, 0.0, 0.0),
        (0.125, 0.5, 0.5),
        (0.25, 0.75, 0.75),
        (0.375, 0.5, 0.5),
        (0.5, 0.15, 0.15),
        (0.625, 0.0, 0.0),
        (0.75, 0.1, 0.1),
        (0.875, 0.5, 0.5),
        (1.0, 1.0, 1.0),
    ),
    "green": (
        (0.0, 0.0, 0.0),
        (0.125, 0.15, 0.15),
        (0.25, 0.15, 0.15),
        (0.375, 0.2, 0.2),
        (0.5, 0.25, 0.25),
        (0.625, 0.5, 0.5),
        (0.75, 0.75, 0.75),
        (0.875, 0.9, 0.9),
        (1.0, 1.0, 1.0),
    ),
    "red": (
        (0.0, 0.0, 0.0),
        (0.125, 0.15, 0.15),
        (0.25, 0.3, 0.3),
        (0.375, 0.6, 0.6),
        (0.5, 1.0, 1.0),
        (0.625, 0.9, 0.9),
        (0.75, 0.9, 0.9),
        (0.875, 0.9, 0.9),
        (1.0, 1.0, 1.0),
    ),
}


_gist_earth: SegmentedColorMapData = {
    "blue": (
        (0.0, 0.0, 0.0),
        (0.0039, 0.1684, 0.1684),
        (0.0078, 0.2212, 0.2212),
        (0.0275, 0.4329, 0.4329),
        (0.0314, 0.4549, 0.4549),
        (0.2824, 0.5004, 0.5004),
        (0.4667, 0.2748, 0.2748),
        (0.5451, 0.3205, 0.3205),
        (0.7843, 0.3961, 0.3961),
        (0.8941, 0.6651, 0.6651),
        (1.0, 0.9843, 0.9843),
    ),
    "green": (
        (0.0, 0.0, 0.0),
        (0.0275, 0.0, 0.0),
        (0.1098, 0.1893, 0.1893),
        (0.1647, 0.3035, 0.3035),
        (0.2078, 0.3841, 0.3841),
        (0.2824, 0.502, 0.502),
        (0.5216, 0.6397, 0.6397),
        (0.698, 0.7171, 0.7171),
        (0.7882, 0.6392, 0.6392),
        (0.7922, 0.6413, 0.6413),
        (0.8, 0.6447, 0.6447),
        (0.8078, 0.6481, 0.6481),
        (0.8157, 0.6549, 0.6549),
        (0.8667, 0.6991, 0.6991),
        (0.8745, 0.7103, 0.7103),
        (0.8824, 0.7216, 0.7216),
        (0.8902, 0.7323, 0.7323),
        (0.898, 0.743, 0.743),
        (0.9412, 0.8275, 0.8275),
        (0.9569, 0.8635, 0.8635),
        (0.9647, 0.8816, 0.8816),
        (0.9961, 0.9733, 0.9733),
        (1.0, 0.9843, 0.9843),
    ),
    "red": (
        (0.0, 0.0, 0.0),
        (0.2824, 0.1882, 0.1882),
        (0.4588, 0.2714, 0.2714),
        (0.549, 0.4719, 0.4719),
        (0.698, 0.7176, 0.7176),
        (0.7882, 0.7553, 0.7553),
        (1.0, 0.9922, 0.9922),
    ),
}


_gist_ncar: SegmentedColorMapData = {
    "blue": (
        (0.0, 0.502, 0.502),
        (0.051, 0.0222, 0.0222),
        (0.1098, 1.0, 1.0),
        (0.2039, 1.0, 1.0),
        (0.2627, 0.6145, 0.6145),
        (0.3216, 0.0, 0.0),
        (0.4157, 0.0, 0.0),
        (0.4745, 0.2342, 0.2342),
        (0.5333, 0.0, 0.0),
        (0.5804, 0.0, 0.0),
        (0.6314, 0.0549, 0.0549),
        (0.6902, 0.0, 0.0),
        (0.7373, 0.0, 0.0),
        (0.7922, 0.9738, 0.9738),
        (0.8, 1.0, 1.0),
        (0.8431, 1.0, 1.0),
        (0.898, 0.9341, 0.9341),
        (1.0, 0.9961, 0.9961),
    ),
    "green": (
        (0.0, 0.0, 0.0),
        (0.051, 0.3722, 0.3722),
        (0.1059, 0.0, 0.0),
        (0.1569, 0.7202, 0.7202),
        (0.1608, 0.7537, 0.7537),
        (0.1647, 0.7752, 0.7752),
        (0.2157, 1.0, 1.0),
        (0.2588, 0.9804, 0.9804),
        (0.2706, 0.9804, 0.9804),
        (0.3176, 1.0, 1.0),
        (0.3686, 0.8081, 0.8081),
        (0.4275, 1.0, 1.0),
        (0.5216, 1.0, 1.0),
        (0.6314, 0.7292, 0.7292),
        (0.6863, 0.2796, 0.2796),
        (0.7451, 0.0, 0.0),
        (0.7922, 0.0, 0.0),
        (0.8431, 0.1753, 0.1753),
        (0.898, 0.5, 0.5),
        (1.0, 0.9725, 0.9725),
    ),
    "red": (
        (0.0, 0.0, 0.0),
        (0.3098, 0.0, 0.0),
        (0.3725, 0.3993, 0.3993),
        (0.4235, 0.5003, 0.5003),
        (0.5333, 1.0, 1.0),
        (0.7922, 1.0, 1.0),
        (0.8471, 0.6218, 0.6218),
        (0.898, 0.9235, 0.9235),
        (1.0, 0.9961, 0.9961),
    ),
}


_gist_stern: SegmentedColorMapData = {
    "blue": (
        (0.0, 0.0, 0.0),
        (0.5, 1.0, 1.0),
        (0.735, 0.0, 0.0),
        (1.0, 1.0, 1.0),
    ),
    "green": ((0, 0, 0), (1, 1, 1)),
    "red": (
        (0.0, 0.0, 0.0),
        (0.0547, 1.0, 1.0),
        (0.25, 0.027, 0.25),
        (1.0, 1.0, 1.0),
    ),
}

_jet: SegmentedColorMapData = {
    "blue": (
        (0.0, 0.5, 0.5),
        (0.11, 1, 1),
        (0.34, 1, 1),
        (0.65, 0, 0),
        (1.0, 0, 0),
    ),
    "green": (
        (0.0, 0, 0),
        (0.125, 0, 0),
        (0.375, 1, 1),
        (0.64, 1, 1),
        (0.91, 0, 0),
        (1.0, 0, 0),
    ),
    "red": (
        (0.0, 0, 0),
        (0.35, 0, 0),
        (0.66, 1, 1),
        (0.89, 1, 1),
        (1.0, 0.5, 0.5),
    ),
}

_nipy_spectral: SegmentedColorMapData = {
    "red": (
        (0.0, 0.0, 0.0),
        (0.05, 0.4667, 0.4667),
        (0.10, 0.5333, 0.5333),
        (0.15, 0.0, 0.0),
        (0.20, 0.0, 0.0),
        (0.25, 0.0, 0.0),
        (0.30, 0.0, 0.0),
        (0.35, 0.0, 0.0),
        (0.40, 0.0, 0.0),
        (0.45, 0.0, 0.0),
        (0.50, 0.0, 0.0),
        (0.55, 0.0, 0.0),
        (0.60, 0.0, 0.0),
        (0.65, 0.7333, 0.7333),
        (0.70, 0.9333, 0.9333),
        (0.75, 1.0, 1.0),
        (0.80, 1.0, 1.0),
        (0.85, 1.0, 1.0),
        (0.90, 0.8667, 0.8667),
        (0.95, 0.80, 0.80),
        (1.0, 0.80, 0.80),
    ),
    "green": (
        (0.0, 0.0, 0.0),
        (0.05, 0.0, 0.0),
        (0.10, 0.0, 0.0),
        (0.15, 0.0, 0.0),
        (0.20, 0.0, 0.0),
        (0.25, 0.4667, 0.4667),
        (0.30, 0.6000, 0.6000),
        (0.35, 0.6667, 0.6667),
        (0.40, 0.6667, 0.6667),
        (0.45, 0.6000, 0.6000),
        (0.50, 0.7333, 0.7333),
        (0.55, 0.8667, 0.8667),
        (0.60, 1.0, 1.0),
        (0.65, 1.0, 1.0),
        (0.70, 0.9333, 0.9333),
        (0.75, 0.8000, 0.8000),
        (0.80, 0.6000, 0.6000),
        (0.85, 0.0, 0.0),
        (0.90, 0.0, 0.0),
        (0.95, 0.0, 0.0),
        (1.0, 0.80, 0.80),
    ),
    "blue": (
        (0.0, 0.0, 0.0),
        (0.05, 0.5333, 0.5333),
        (0.10, 0.6000, 0.6000),
        (0.15, 0.6667, 0.6667),
        (0.20, 0.8667, 0.8667),
        (0.25, 0.8667, 0.8667),
        (0.30, 0.8667, 0.8667),
        (0.35, 0.6667, 0.6667),
        (0.40, 0.5333, 0.5333),
        (0.45, 0.0, 0.0),
        (0.5, 0.0, 0.0),
        (0.55, 0.0, 0.0),
        (0.60, 0.0, 0.0),
        (0.65, 0.0, 0.0),
        (0.70, 0.0, 0.0),
        (0.75, 0.0, 0.0),
        (0.80, 0.0, 0.0),
        (0.85, 0.0, 0.0),
        (0.90, 0.0, 0.0),
        (0.95, 0.0, 0.0),
        (1.0, 0.80, 0.80),
    ),
}

_turbo = (
    (0.18995, 0.07176, 0.23217),
    (0.19483, 0.08339, 0.26149),
    (0.19956, 0.09498, 0.29024),
    (0.20415, 0.10652, 0.31844),
    (0.20860, 0.11802, 0.34607),
    (0.21291, 0.12947, 0.37314),
    (0.21708, 0.14087, 0.39964),
    (0.22111, 0.15223, 0.42558),
    (0.22500, 0.16354, 0.45096),
    (0.22875, 0.17481, 0.47578),
    (0.23236, 0.18603, 0.50004),
    (0.23582, 0.19720, 0.52373),
    (0.23915, 0.20833, 0.54686),
    (0.24234, 0.21941, 0.56942),
    (0.24539, 0.23044, 0.59142),
    (0.24830, 0.24143, 0.61286),
    (0.25107, 0.25237, 0.63374),
    (0.25369, 0.26327, 0.65406),
    (0.25618, 0.27412, 0.67381),
    (0.25853, 0.28492, 0.69300),
    (0.26074, 0.29568, 0.71162),
    (0.26280, 0.30639, 0.72968),
    (0.26473, 0.31706, 0.74718),
    (0.26652, 0.32768, 0.76412),
    (0.26816, 0.33825, 0.78050),
    (0.26967, 0.34878, 0.79631),
    (0.27103, 0.35926, 0.81156),
    (0.27226, 0.36970, 0.82624),
    (0.27334, 0.38008, 0.84037),
    (0.27429, 0.39043, 0.85393),
    (0.27509, 0.40072, 0.86692),
    (0.27576, 0.41097, 0.87936),
    (0.27628, 0.42118, 0.89123),
    (0.27667, 0.43134, 0.90254),
    (0.27691, 0.44145, 0.91328),
    (0.27701, 0.45152, 0.92347),
    (0.27698, 0.46153, 0.93309),
    (0.27680, 0.47151, 0.94214),
    (0.27648, 0.48144, 0.95064),
    (0.27603, 0.49132, 0.95857),
    (0.27543, 0.50115, 0.96594),
    (0.27469, 0.51094, 0.97275),
    (0.27381, 0.52069, 0.97899),
    (0.27273, 0.53040, 0.98461),
    (0.27106, 0.54015, 0.98930),
    (0.26878, 0.54995, 0.99303),
    (0.26592, 0.55979, 0.99583),
    (0.26252, 0.56967, 0.99773),
    (0.25862, 0.57958, 0.99876),
    (0.25425, 0.58950, 0.99896),
    (0.24946, 0.59943, 0.99835),
    (0.24427, 0.60937, 0.99697),
    (0.23874, 0.61931, 0.99485),
    (0.23288, 0.62923, 0.99202),
    (0.22676, 0.63913, 0.98851),
    (0.22039, 0.64901, 0.98436),
    (0.21382, 0.65886, 0.97959),
    (0.20708, 0.66866, 0.97423),
    (0.20021, 0.67842, 0.96833),
    (0.19326, 0.68812, 0.96190),
    (0.18625, 0.69775, 0.95498),
    (0.17923, 0.70732, 0.94761),
    (0.17223, 0.71680, 0.93981),
    (0.16529, 0.72620, 0.93161),
    (0.15844, 0.73551, 0.92305),
    (0.15173, 0.74472, 0.91416),
    (0.14519, 0.75381, 0.90496),
    (0.13886, 0.76279, 0.89550),
    (0.13278, 0.77165, 0.88580),
    (0.12698, 0.78037, 0.87590),
    (0.12151, 0.78896, 0.86581),
    (0.11639, 0.79740, 0.85559),
    (0.11167, 0.80569, 0.84525),
    (0.10738, 0.81381, 0.83484),
    (0.10357, 0.82177, 0.82437),
    (0.10026, 0.82955, 0.81389),
    (0.09750, 0.83714, 0.80342),
    (0.09532, 0.84455, 0.79299),
    (0.09377, 0.85175, 0.78264),
    (0.09287, 0.85875, 0.77240),
    (0.09267, 0.86554, 0.76230),
    (0.09320, 0.87211, 0.75237),
    (0.09451, 0.87844, 0.74265),
    (0.09662, 0.88454, 0.73316),
    (0.09958, 0.89040, 0.72393),
    (0.10342, 0.89600, 0.71500),
    (0.10815, 0.90142, 0.70599),
    (0.11374, 0.90673, 0.69651),
    (0.12014, 0.91193, 0.68660),
    (0.12733, 0.91701, 0.67627),
    (0.13526, 0.92197, 0.66556),
    (0.14391, 0.92680, 0.65448),
    (0.15323, 0.93151, 0.64308),
    (0.16319, 0.93609, 0.63137),
    (0.17377, 0.94053, 0.61938),
    (0.18491, 0.94484, 0.60713),
    (0.19659, 0.94901, 0.59466),
    (0.20877, 0.95304, 0.58199),
    (0.22142, 0.95692, 0.56914),
    (0.23449, 0.96065, 0.55614),
    (0.24797, 0.96423, 0.54303),
    (0.26180, 0.96765, 0.52981),
    (0.27597, 0.97092, 0.51653),
    (0.29042, 0.97403, 0.50321),
    (0.30513, 0.97697, 0.48987),
    (0.32006, 0.97974, 0.47654),
    (0.33517, 0.98234, 0.46325),
    (0.35043, 0.98477, 0.45002),
    (0.36581, 0.98702, 0.43688),
    (0.38127, 0.98909, 0.42386),
    (0.39678, 0.99098, 0.41098),
    (0.41229, 0.99268, 0.39826),
    (0.42778, 0.99419, 0.38575),
    (0.44321, 0.99551, 0.37345),
    (0.45854, 0.99663, 0.36140),
    (0.47375, 0.99755, 0.34963),
    (0.48879, 0.99828, 0.33816),
    (0.50362, 0.99879, 0.32701),
    (0.51822, 0.99910, 0.31622),
    (0.53255, 0.99919, 0.30581),
    (0.54658, 0.99907, 0.29581),
    (0.56026, 0.99873, 0.28623),
    (0.57357, 0.99817, 0.27712),
    (0.58646, 0.99739, 0.26849),
    (0.59891, 0.99638, 0.26038),
    (0.61088, 0.99514, 0.25280),
    (0.62233, 0.99366, 0.24579),
    (0.63323, 0.99195, 0.23937),
    (0.64362, 0.98999, 0.23356),
    (0.65394, 0.98775, 0.22835),
    (0.66428, 0.98524, 0.22370),
    (0.67462, 0.98246, 0.21960),
    (0.68494, 0.97941, 0.21602),
    (0.69525, 0.97610, 0.21294),
    (0.70553, 0.97255, 0.21032),
    (0.71577, 0.96875, 0.20815),
    (0.72596, 0.96470, 0.20640),
    (0.73610, 0.96043, 0.20504),
    (0.74617, 0.95593, 0.20406),
    (0.75617, 0.95121, 0.20343),
    (0.76608, 0.94627, 0.20311),
    (0.77591, 0.94113, 0.20310),
    (0.78563, 0.93579, 0.20336),
    (0.79524, 0.93025, 0.20386),
    (0.80473, 0.92452, 0.20459),
    (0.81410, 0.91861, 0.20552),
    (0.82333, 0.91253, 0.20663),
    (0.83241, 0.90627, 0.20788),
    (0.84133, 0.89986, 0.20926),
    (0.85010, 0.89328, 0.21074),
    (0.85868, 0.88655, 0.21230),
    (0.86709, 0.87968, 0.21391),
    (0.87530, 0.87267, 0.21555),
    (0.88331, 0.86553, 0.21719),
    (0.89112, 0.85826, 0.21880),
    (0.89870, 0.85087, 0.22038),
    (0.90605, 0.84337, 0.22188),
    (0.91317, 0.83576, 0.22328),
    (0.92004, 0.82806, 0.22456),
    (0.92666, 0.82025, 0.22570),
    (0.93301, 0.81236, 0.22667),
    (0.93909, 0.80439, 0.22744),
    (0.94489, 0.79634, 0.22800),
    (0.95039, 0.78823, 0.22831),
    (0.95560, 0.78005, 0.22836),
    (0.96049, 0.77181, 0.22811),
    (0.96507, 0.76352, 0.22754),
    (0.96931, 0.75519, 0.22663),
    (0.97323, 0.74682, 0.22536),
    (0.97679, 0.73842, 0.22369),
    (0.98000, 0.73000, 0.22161),
    (0.98289, 0.72140, 0.21918),
    (0.98549, 0.71250, 0.21650),
    (0.98781, 0.70330, 0.21358),
    (0.98986, 0.69382, 0.21043),
    (0.99163, 0.68408, 0.20706),
    (0.99314, 0.67408, 0.20348),
    (0.99438, 0.66386, 0.19971),
    (0.99535, 0.65341, 0.19577),
    (0.99607, 0.64277, 0.19165),
    (0.99654, 0.63193, 0.18738),
    (0.99675, 0.62093, 0.18297),
    (0.99672, 0.60977, 0.17842),
    (0.99644, 0.59846, 0.17376),
    (0.99593, 0.58703, 0.16899),
    (0.99517, 0.57549, 0.16412),
    (0.99419, 0.56386, 0.15918),
    (0.99297, 0.55214, 0.15417),
    (0.99153, 0.54036, 0.14910),
    (0.98987, 0.52854, 0.14398),
    (0.98799, 0.51667, 0.13883),
    (0.98590, 0.50479, 0.13367),
    (0.98360, 0.49291, 0.12849),
    (0.98108, 0.48104, 0.12332),
    (0.97837, 0.46920, 0.11817),
    (0.97545, 0.45740, 0.11305),
    (0.97234, 0.44565, 0.10797),
    (0.96904, 0.43399, 0.10294),
    (0.96555, 0.42241, 0.09798),
    (0.96187, 0.41093, 0.09310),
    (0.95801, 0.39958, 0.08831),
    (0.95398, 0.38836, 0.08362),
    (0.94977, 0.37729, 0.07905),
    (0.94538, 0.36638, 0.07461),
    (0.94084, 0.35566, 0.07031),
    (0.93612, 0.34513, 0.06616),
    (0.93125, 0.33482, 0.06218),
    (0.92623, 0.32473, 0.05837),
    (0.92105, 0.31489, 0.05475),
    (0.91572, 0.30530, 0.05134),
    (0.91024, 0.29599, 0.04814),
    (0.90463, 0.28696, 0.04516),
    (0.89888, 0.27824, 0.04243),
    (0.89298, 0.26981, 0.03993),
    (0.88691, 0.26152, 0.03753),
    (0.88066, 0.25334, 0.03521),
    (0.87422, 0.24526, 0.03297),
    (0.86760, 0.23730, 0.03082),
    (0.86079, 0.22945, 0.02875),
    (0.85380, 0.22170, 0.02677),
    (0.84662, 0.21407, 0.02487),
    (0.83926, 0.20654, 0.02305),
    (0.83172, 0.19912, 0.02131),
    (0.82399, 0.19182, 0.01966),
    (0.81608, 0.18462, 0.01809),
    (0.80799, 0.17753, 0.01660),
    (0.79971, 0.17055, 0.01520),
    (0.79125, 0.16368, 0.01387),
    (0.78260, 0.15693, 0.01264),
    (0.77377, 0.15028, 0.01148),
    (0.76476, 0.14374, 0.01041),
    (0.75556, 0.13731, 0.00942),
    (0.74617, 0.13098, 0.00851),
    (0.73661, 0.12477, 0.00769),
    (0.72686, 0.11867, 0.00695),
    (0.71692, 0.11268, 0.00629),
    (0.70680, 0.10680, 0.00571),
    (0.69650, 0.10102, 0.00522),
    (0.68602, 0.09536, 0.00481),
    (0.67535, 0.08980, 0.00449),
    (0.66449, 0.08436, 0.00424),
    (0.65345, 0.07902, 0.00408),
    (0.64223, 0.07380, 0.00401),
    (0.63082, 0.06868, 0.00401),
    (0.61923, 0.06367, 0.00410),
    (0.60746, 0.05878, 0.00427),
    (0.59550, 0.05399, 0.00453),
    (0.58336, 0.04931, 0.00486),
    (0.57103, 0.04474, 0.00529),
    (0.55852, 0.04028, 0.00579),
    (0.54583, 0.03593, 0.00638),
    (0.53295, 0.03169, 0.00705),
    (0.51989, 0.02756, 0.00780),
    (0.50664, 0.02354, 0.00863),
    (0.49321, 0.01963, 0.00955),
    (0.47960, 0.01583, 0.01055),
)

autumn = SegmentInterpolatedMap(_autumn, kind=cmk.sequential)
binary = SegmentInterpolatedMap(_binary, kind=cmk.sequential)
bone = SegmentInterpolatedMap(_bone, kind=cmk.sequential)
cool = SegmentInterpolatedMap(_cool, kind=cmk.sequential)
copper = SegmentInterpolatedMap(_copper, kind=cmk.sequential)
gray = SegmentInterpolatedMap(_gray, kind=cmk.sequential)
hot = SegmentInterpolatedMap(_hot, kind=cmk.sequential)
pink = SegmentInterpolatedMap(_pink, kind=cmk.sequential)
spring = SegmentInterpolatedMap(_spring, kind=cmk.sequential)
summer = SegmentInterpolatedMap(_summer, kind=cmk.sequential)
winter = SegmentInterpolatedMap(_winter, kind=cmk.sequential)
Wistia = SegmentInterpolatedMap(_wistia, kind=cmk.sequential)
coolwarm = SegmentInterpolatedMap(_coolwarm, kind=cmk.diverging)
hsv = SegmentInterpolatedMap(_hsv, kind=cmk.cyclic)

# miscellaneous
CMRmap = SegmentInterpolatedMap(_CMRmap)
gist_earth = SegmentInterpolatedMap(_gist_earth)
gist_ncar = SegmentInterpolatedMap(_gist_ncar)
gist_stern = SegmentInterpolatedMap(_gist_stern)
jet = SegmentInterpolatedMap(_jet)
nipy_spectral = SegmentInterpolatedMap(_nipy_spectral)