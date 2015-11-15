from sdl2._sdl2 import ffi, lib
from error import check_int_err


class Surface(object):
    """A collection of pixels used in software blitting."""

    @staticmethod
    def _from_ptr(ptr):
        surface = object.__new__(Surface)
        surface._ptr = ptr
        return surface

    @staticmethod
    def from_image(path):
        surface = object.__new__(Surface)
        surface._ptr = lib.IMG_Load(path)
        return surface

    def __del__(self):
        lib.SDL_FreeSurface(self._ptr)

    @property
    def w(self):
        """int: The width of the surface."""
        return self._ptr.contents.w

    @property
    def h(self):
        """int: The height of the surface."""
        return self._ptr.contents.h

    def blit(self, src_rect, dst_surf, dst_rect):
        """Performs a fast blit from the source surface to the destination surface.
        This assumes that the source and destination rectangles are
        the same size.  If either src_rect or dst_rect are None, the entire
        surface is copied.  The final blit rectangles are saved
        in src_rect and dst_rect after all clipping is performed.

        Args:
            src_rect (Rect): Source rect.
            dst_surf (Surface): Destination surface.
            dst_rect (Rect): Destination rect.

        Raises:
            SDLError: If the blit fails.
        """
        check_int_err(lib.SDL_UpperBlit(self._ptr, src_rect._ptr, dst_surf._ptr, dst_rect._ptr))

    def lock(self):
        check_int_err(lib.SDL_LockSurface(self._ptr))

    def unlock(self):
        lib.SDL_UnlockSurface(self._ptr)
