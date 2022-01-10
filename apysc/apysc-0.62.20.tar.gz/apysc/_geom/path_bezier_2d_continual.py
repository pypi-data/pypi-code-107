"""Path data class implementation for the svg's
`continual 2D bezier curve` (T).
"""

from typing import Union

from apysc._geom.path_data_base import PathDataBase
from apysc._geom.path_x_interface import PathXInterface
from apysc._geom.path_y_interface import PathYInterface
from apysc._type.boolean import Boolean
from apysc._type.int import Int
from apysc._type.string import String


class PathBezier2DContinual(PathDataBase, PathXInterface, PathYInterface):
    """
    Path data class for the svg's `continual 2D bezier curve` (T).
    """

    def __init__(
            self, x: Union[int, Int], y: Union[int, Int], *,
            relative: Union[bool, Boolean] = False) -> None:
        """
        Path data class for the svg's `continual 2D bezier curve` (T).

        Parameters
        ----------
        x : int or Int
            X-coordinate of the destination point.
        y : int or Int
            Y-coordinate of the destination point.
        relative : bool or Boolean, default False
            The boolean value indicating whether the path
            coordinates are relative or not (absolute).
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='__init__', locals_=locals(),
                module_name=__name__, class_=PathBezier2DContinual):
            from apysc._converter.to_apysc_val_from_builtin import \
                get_copied_int_from_builtin_val
            from apysc._geom.path_label import PathLabel
            super(PathBezier2DContinual, self).__init__(
                path_label=PathLabel.BEZIER_2D_CONTINUAL,
                relative=relative)
            self.x = get_copied_int_from_builtin_val(integer=x)
            self.y = get_copied_int_from_builtin_val(integer=y)

    def _get_svg_str(self) -> str:
        """
        Get a path's SVG string created with the current setting.

        Returns
        -------
        svg_str : str
            A path's SVG string created with the current setting.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_=self._get_svg_str, locals_=locals(),
                module_name=__name__, class_=PathBezier2DContinual):
            from apysc._type import value_util
            svg_char: String = self._get_svg_char()
            svg_char_str: str = value_util.get_value_str_for_expression(
                value=svg_char)
            x_str: str = value_util.get_value_str_for_expression(
                value=self._x)
            y_str: str = value_util.get_value_str_for_expression(
                value=self._y)
            svg_str: str = (
                f'{svg_char_str} + String({x_str}) + " " + String({y_str})')
            return svg_str

    def update_path_data(
            self, x: Union[int, Int], y: Union[int, Int],
            relative: Union[bool, Boolean]) -> None:
        """
        Update the path's data settings.

        Parameters
        ----------
        x : int or Int
            X-coordinate of the destination point.
        y : int or Int
            Y-coordinate of the destination point.
        relative : bool or Boolean, default False
            The boolean value indicating whether the path
            coordinates are relative or not (absolute).
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_=self.update_path_data, locals_=locals(),
                module_name=__name__, class_=PathBezier2DContinual):
            from apysc._converter.to_apysc_val_from_builtin import \
                get_copied_boolean_from_builtin_val
            from apysc._converter.to_apysc_val_from_builtin import \
                get_copied_int_from_builtin_val
            self.x = get_copied_int_from_builtin_val(integer=x)
            self.y = get_copied_int_from_builtin_val(integer=y)
            self.relative = get_copied_boolean_from_builtin_val(
                bool_val=relative)
