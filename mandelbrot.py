#!/usr/bin/env python3

def mandelbrot_ascii(
    width=80,
    height=24,
    max_iterations=100,
    re_start=-2.0,
    re_end=1.0,
    im_start=-1.0,
    im_end=1.0
):
    """
    Generate an ASCII representation of the Mandelbrot set.

    :param width: Number of characters to represent horizontal span.
    :param height: Number of text rows in the output.
    :param max_iterations: Maximum iterations for determining set membership.
    :param re_start: Start of the real axis range.
    :param re_end: End of the real axis range.
    :param im_start: Start of the imaginary axis range.
    :param im_end: End of the imaginary axis range.
    :return: A string that contains the ASCII art for the Mandelbrot set.
    """
    # A list of characters that indicate intensity:
    # from ' ' (empty) for fast escape, to '@' for points that remain longer (or never escape).
    ascii_gradient = " .:-=+*#%@" 

    # We'll build a list of lines, and then join them at the end.
    output_lines = []

    # Step in real and imaginary axes
    re_step = (re_end - re_start) / (width - 1)
    im_step = (im_end - im_start) / (height - 1)

    for row in range(height):
        # Imaginary part for the current row (top to bottom)
        c_im = im_start + row * im_step
        row_chars = []

        for col in range(width):
            # Real part (left to right)
            c_re = re_start + col * re_step

            # Start iteration at z = 0
            z_re, z_im = 0.0, 0.0
            iteration = 0

            # Mandelbrot iteration
            while z_re*z_re + z_im*z_im <= 4.0 and iteration < max_iterations:
                # z → z² + c
                new_re = z_re*z_re - z_im*z_im + c_re
                new_im = 2.0*z_re*z_im + c_im
                z_re, z_im = new_re, new_im
                iteration += 1

            # Choose a character from the gradient based on iteration count
            # If iteration == max_iterations, treat it as if it's still "in the set."
            if iteration == max_iterations:
                char = ascii_gradient[-1]
            else:
                # Scale iteration to the range of indices in ascii_gradient
                char = ascii_gradient[int(iteration / max_iterations * (len(ascii_gradient) - 1))]

            row_chars.append(char)

        # Join this row of characters and add it to our output
        output_lines.append("".join(row_chars))

    return "\n".join(output_lines)

def main():
    art = mandelbrot_ascii(
        width=80,
        height=24,
        max_iterations=100,
        re_start=-2.0,
        re_end=1.0,
        im_start=-1.0,
        im_end=1.0
    )
    print(art)

if __name__ == "__main__":
    main()