# resnet_explainer.py


import numpy as np
from manim import *


class IntroductionScene(Scene):
    def construct(self):
        title = Text("Learning: ResNet functionality", font_size=56).to_edge(UP)

        # Simple diagram: x -> [ f ] -> y
        x_label = Text("x", font_size=48).move_to(LEFT * 3)

        box = Rectangle(width=2.4, height=1.4, color=BLUE).set_fill(BLUE, 0.2)
        box.move_to(ORIGIN)
        box_label = Text("f", font_size=48).move_to(box.get_center())

        y_label = Text("y", font_size=48).move_to(RIGHT * 3)

        arrow_in = Arrow(start=x_label.get_right(), end=box.get_left(), buff=0.1)
        arrow_out = Arrow(start=box.get_right(), end=y_label.get_left(), buff=0.1)

        eq = Text("y = f(x)", font_size=40).next_to(box, DOWN, buff=0.6)
        subtitle = Text(
            "We see input x and output y — can we discover f?",
            font_size=30,
        ).to_edge(DOWN)

        # Slower, more deliberate pacing
        self.play(Write(title, run_time=1.0))
        self.wait(0.5)

        self.play(
            FadeIn(x_label, run_time=0.5),
            FadeIn(box, run_time=0.5),
            FadeIn(box_label, run_time=0.5),
            Create(arrow_in, run_time=0.5),
            Create(arrow_out, run_time=0.5),
            FadeIn(y_label, run_time=0.5),
            Write(eq, run_time=0.5),
        )
        self.wait(0.5)

        self.play(Write(subtitle, run_time=0.5))
        self.wait(2.0)


class ImageExample(Scene):
    def construct(self):
        # Title and simple blurry->f->sharp image example
        title = Text("A practical example for ResNet:", font_size=42).to_edge(UP)
        self.play(Write(title, run_time=1.0))

        # Left: blurry image, Center: function box f, Right: sharp image
        img_blur = (
            ImageMobject("assets/blury.png").scale(1.05).to_edge(LEFT).shift(DOWN * 0.2)
        )
        img_sharp = (
            ImageMobject("assets/normal.png")
            .scale(1.05)
            .to_edge(RIGHT)
            .shift(DOWN * 0.2)
        )

        box = (
            Rectangle(width=2.0, height=1.6, color=BLUE)
            .set_fill(BLUE, 0.15)
            .move_to(ORIGIN + DOWN * 0.2)
        )
        box_label = Text("f", font_size=48).move_to(box.get_center())

        arrow_in = Arrow(start=img_blur.get_right(), end=box.get_left(), buff=0.15)
        arrow_out = Arrow(start=box.get_right(), end=img_sharp.get_left(), buff=0.15)

        credit = Text(
            "Image credit: https://www.vizuaranewsletter.com/p/resnet-the-architecture-that-changed",
            font_size=18,
        ).to_edge(DOWN)

        # Sequence: blurry image appears, arrow to f, f appears, arrow to sharp, sharp appears
        self.play(FadeIn(img_blur, run_time=0.5))

        # create arrow pointing to where the box will be (box exists but not yet shown)
        # box and box_label are already defined; create arrow to its position
        self.play(Create(arrow_in, run_time=0.5))

        # reveal the function box f
        self.play(FadeIn(box, box_label, run_time=0.5))

        # arrow from f to sharp image, then reveal sharp image (keep blur and f visible)
        self.play(Create(arrow_out, run_time=0.5))
        self.play(FadeIn(img_sharp, run_time=0.5))

        # show credit
        self.play(Write(credit, run_time=0.5))

        # finish
        self.wait(2.0)


class WhatIsF(Scene):
    def construct(self):
        # Question at top
        # 1) show the question, then remove it
        question = Text("So what exactly is in this f block?", font_size=44).to_edge(UP)
        self.play(Write(question, run_time=1.2))
        self.wait(0.5)
        self.play(FadeOut(question, run_time=0.6))

        # 2) brief statement: ResNet simplified view (5 layers)
        info = Text(
            "For ResNet (simplified): f can include 5 stacked layers", font_size=30
        ).to_edge(UP)
        self.play(Write(info, run_time=1.0))
        self.wait(0.5)

        # 3) show x, then animate through 5 layers one at a time, then y
        x = Text("x", font_size=36).to_edge(LEFT).shift(DOWN * 0.2)

        # Create five small layer boxes, arrange horizontally
        layers = (
            VGroup(
                *[
                    Rectangle(width=1.0, height=0.6, color=GREEN).set_fill(GREEN, 0.3)
                    for _ in range(5)
                ]
            )
            .arrange(RIGHT, buff=0.6)
            .move_to(ORIGIN + DOWN * 0.2)
        )

        # Labels for layers
        layer_labels = VGroup(*[Text(f"L{i+1}", font_size=20) for i in range(5)])
        for lab, box in zip(layer_labels, layers):
            lab.move_to(box.get_center())

        y = Text("y", font_size=36).to_edge(RIGHT).shift(DOWN * 0.2)

        # Show x and all L1..L5 together with connecting arrows
        self.play(FadeIn(x, run_time=0.8))

        # create chain arrows between x -> L1 -> L2 -> ... -> L5 -> y
        arrows = []
        prev_right = x.get_right()
        for box in layers:
            arrows.append(Arrow(start=prev_right, end=box.get_left(), buff=0.1))
            prev_right = box.get_right()
        arrow_final = Arrow(start=prev_right, end=y.get_left(), buff=0.1)

        # show all small L blocks, their labels, and all arrows at once
        self.play(
            Create(VGroup(*arrows), run_time=1.0),
            Create(arrow_final, run_time=1.0),
            FadeIn(layers, layer_labels, run_time=1.0),
        )

        # show y as well
        self.play(FadeIn(y, run_time=0.6))
        self.wait(0.5)

        # Transform each L_i into its specific taller block one by one, removing the L# label
        func_names = ["Conv", "BN", "ReLU", "Conv", "BN"]
        func_colors = [GREEN, TEAL, ORANGE, GREEN, TEAL]

        for old_box, lab, name, color in zip(
            layers, layer_labels, func_names, func_colors
        ):
            new_block = Rectangle(width=1.2, height=1.4, color=color).set_fill(
                color, 0.35
            )
            new_block.move_to(old_box.get_center())
            new_label = Text(name, font_size=18).move_to(new_block.get_center())

            self.play(ReplacementTransform(old_box, new_block, run_time=0.5))
            self.play(FadeOut(lab, run_time=0.35), FadeIn(new_label, run_time=0.5))

        # small pause after transformation
        self.wait(1.0)


class ResidualConnection(Scene):
    def construct(self):
        # Title explaining limitations
        title = Text("But this isn't enough — why?", font_size=44).to_edge(UP)
        sub = Text(
            "Vanishing/exploding gradients and optimization difficulties", font_size=24
        ).next_to(title, DOWN, buff=0.2)

        self.play(Write(title, run_time=1.0))
        self.play(Write(sub, run_time=1.0))
        self.wait(0.6)

        # Build diagram: x -> five function blocks -> (+) -> y with arrows
        x = Text("x", font_size=36).to_edge(LEFT).shift(DOWN * 0.2)
        func_names = ["Conv", "BN", "ReLU", "Conv", "BN"]
        func_colors = [GREEN, TEAL, ORANGE, GREEN, TEAL]
        blocks = []
        labels = []
        for name, color in zip(func_names, func_colors):
            r = Rectangle(width=1.2, height=1.0, color=color).set_fill(color, 0.25)
            lbl = Text(name, font_size=18).move_to(r.get_center())
            blocks.append(r)
            labels.append(lbl)

        layers = VGroup(*blocks).arrange(RIGHT, buff=0.6).move_to(ORIGIN + DOWN * 0.2)
        for box, lab in zip(layers, labels):
            lab.move_to(box.get_center())

        y = Text("y", font_size=36).to_edge(RIGHT).shift(DOWN * 0.2)

        # add-circle (plus) between last block and y
        add_pos = layers[-1].get_right() + RIGHT * 0.6
        add_circle = (
            Circle(radius=0.26, color=YELLOW).set_fill(YELLOW, 0.06).move_to(add_pos)
        )
        plus = Text("+", font_size=26).move_to(add_circle.get_center())

        # prepare white forward arrows
        fwd_arrows = []
        prev = x.get_right()
        for box in layers:
            fwd_arrows.append(
                Arrow(start=prev, end=box.get_left(), buff=0.1).set_color(WHITE)
            )
            prev = box.get_right()
        arrow_to_add = Arrow(start=prev, end=add_circle.get_left(), buff=0.1).set_color(
            WHITE
        )
        arrow_add_to_y = Arrow(
            start=add_circle.get_right(), end=y.get_left(), buff=0.1
        ).set_color(WHITE)

        # create an L-shaped elbow that goes UP from x, then HORIZONTAL, then DOWN into add_circle
        # make it higher and extend farther right before descending to the top-center
        up_offset = 1.0
        # start at the top-center of `x`, then go further up to `top_point`
        start_up = x.get_top()
        top_point = start_up + UP * up_offset
        # compute horizontal end aligned with the add_circle center x, at the top_point's y
        horiz_end = np.array([add_circle.get_center()[0], top_point[1], top_point[2]])
        elbow_up = Line(start=start_up, end=top_point).set_color(WHITE)
        elbow_across = Line(start=top_point, end=horiz_end).set_color(WHITE)
        # descend into the top center of the add_circle
        elbow_down = Arrow(
            start=horiz_end, end=add_circle.get_top(), buff=0.0
        ).set_color(WHITE)

        # show everything simultaneously
        self.play(
            FadeIn(x, run_time=0.6),
            FadeIn(layers, run_time=0.8),
            *[FadeIn(lab, run_time=0.5) for lab in labels],
            FadeIn(add_circle, plus, run_time=0.6),
            FadeIn(y, run_time=0.6),
            Create(VGroup(*fwd_arrows), run_time=0.9),
            Create(arrow_to_add, run_time=0.9),
            # elbow will be drawn after the main reveal
            Create(arrow_add_to_y, run_time=0.9),
        )
        self.wait(1.2)

        # draw the elbow arrow after the rest of the diagram is visible
        self.play(
            Create(elbow_up, run_time=0.5),
            Create(elbow_across, run_time=0.6),
            Create(elbow_down, run_time=0.6),
        )
        self.wait(0.4)

        # short explanatory note
        note = Text(
            "Deep stacks can cause gradients to vanish/explode; skip connections help.",
            font_size=20,
        ).to_edge(DOWN)
        self.play(Write(note, run_time=1.0))
        self.wait(2.0)


class ResidualExplanation(Scene):
    def construct(self):
        # Draw the residual diagram at the top and explain why it helps
        title = Text("Why skip connections help", font_size=44).to_edge(UP)
        self.play(Write(title, run_time=1.0))

        # Diagram placed near the top
        diagram_y = UP * 1.0

        # x, five function blocks, add circle, y
        func_names = ["Conv", "BN", "ReLU", "Conv", "BN"]
        func_colors = [GREEN, TEAL, ORANGE, GREEN, TEAL]
        blocks = []
        labels = []
        for name, color in zip(func_names, func_colors):
            r = Rectangle(width=1.2, height=1.0, color=color).set_fill(color, 0.25)
            lbl = Text(name, font_size=16).move_to(r.get_center())
            blocks.append(r)
            labels.append(lbl)

        layers = VGroup(*blocks).arrange(RIGHT, buff=0.6).move_to(diagram_y)
        for box, lab in zip(layers, labels):
            lab.move_to(box.get_center())

        x = Text("x", font_size=32).move_to(layers.get_left() + LEFT * 1.4)
        y = Text("y", font_size=32).move_to(layers.get_right() + RIGHT * 1.4)

        add_pos = layers[-1].get_right() + RIGHT * 0.6
        add_circle = (
            Circle(radius=0.26, color=YELLOW).set_fill(YELLOW, 0.06).move_to(add_pos)
        )
        plus = Text("+", font_size=26).move_to(add_circle.get_center())

        # forward arrows
        fwd_arrows = []
        prev = x.get_right()
        for box in layers:
            fwd_arrows.append(
                Arrow(start=prev, end=box.get_left(), buff=0.1).set_color(WHITE)
            )
            prev = box.get_right()
        arrow_to_add = Arrow(start=prev, end=add_circle.get_left(), buff=0.1).set_color(
            WHITE
        )
        arrow_add_to_y = Arrow(
            start=add_circle.get_right(), end=y.get_left(), buff=0.1
        ).set_color(WHITE)

        # draw diagram (without elbow) first
        self.play(
            FadeIn(x, run_time=0.6),
            FadeIn(layers, run_time=0.8),
            *[FadeIn(lab, run_time=0.4) for lab in labels],
            FadeIn(add_circle, plus, run_time=0.6),
            FadeIn(y, run_time=0.6),
            Create(VGroup(*fwd_arrows), run_time=0.9),
            Create(arrow_to_add, run_time=0.9),
            Create(arrow_add_to_y, run_time=0.9),
        )
        self.wait(0.6)
        # Show the algebraic identity and a short explanation bullets
        # Draw an identity skip arrow (elbow) from x to the add circle so the
        # direct path is visible. Recompute coordinates now that layout is final.
        up_offset = 0.9
        start_up = x.get_top()
        top_point = start_up + UP * up_offset
        horiz_end = np.array([add_circle.get_center()[0], top_point[1], top_point[2]])
        skip_up = (
            Line(start=start_up, end=top_point).set_color(WHITE).set_stroke(width=5)
        )
        skip_across = (
            Line(start=top_point, end=horiz_end).set_color(WHITE).set_stroke(width=5)
        )
        skip_down = (
            Arrow(start=horiz_end, end=add_circle.get_top(), buff=0.0)
            .set_color(WHITE)
            .set_stroke(width=5)
        )
        skip_up.set_z_index(10)
        skip_across.set_z_index(10)
        skip_down.set_z_index(10)
        self.play(Create(skip_up, run_time=0.5), Create(skip_across, run_time=0.6))
        self.play(Create(skip_down, run_time=0.6))
        self.wait(0.2)

        # Show the algebraic identity and a short explanation bullets
        eq = Text("y = x + f(x)", font_size=36).next_to(layers, DOWN, buff=0.7)
        self.play(Write(eq, run_time=0.8))
        self.wait(0.4)

        # Explanation lines (appear one by one)
        lines = [
            "Skip connection = identity path from x to output",
            "Provides a direct gradient path, alleviating vanishing gradients",
            "Lets layers learn residuals f(x) instead of full mapping, easing optimization",
        ]

        expl_texts = [
            Text(s, font_size=20).next_to(eq, DOWN, buff=0.6 + i * 0.45)
            for i, s in enumerate(lines)
        ]
        for t in expl_texts:
            self.play(Write(t, run_time=0.7))
            self.wait(0.5)

        # final note and pause
        note = Text(
            "Result: deeper networks train more reliably and perform better.",
            font_size=20,
        ).to_edge(DOWN)
        self.play(Write(note, run_time=0.9))
        self.wait(2.0)


class CNNExample(Scene):
    def construct(self):
        # Title
        title = Text("ResNet: Layer-by-Layer Transformations", font_size=36).to_edge(UP)
        self.play(Write(title, run_time=1.0))
        self.wait(0.5)

        # Create a 3x3 grid representing input pixels
        grid_size = 3
        cell_size = 0.5

        # Helper function to create a grid with values
        def create_grid(values, position, color=BLUE, show_values=True):
            grid_group = VGroup()
            for i in range(grid_size):
                for j in range(grid_size):
                    square = Square(side_length=cell_size, color=color, stroke_width=2)
                    square.move_to(
                        position + np.array([j * cell_size, -i * cell_size, 0])
                    )

                    # Add value text if provided
                    if values is not None and show_values:
                        val = values[i][j]
                        # Normalize for opacity (assuming values 0-100 range)
                        opacity = min(abs(val) / 50.0, 1.0) if val != 0 else 0
                        square.set_fill(color, opacity=opacity * 0.5)
                        # Format value to 1 decimal place
                        text = Text(f"{val:.1f}", font_size=12).move_to(
                            square.get_center()
                        )
                        grid_group.add(VGroup(square, text))
                    else:
                        grid_group.add(square)
            # Center the grid around the provided position so arrows stay horizontal
            grid_group.move_to(position)
            return grid_group

        # Create initial input grid with sample pixel values
        input_values = np.array(
            [
                [10.0, 20.0, 15.0],
                [25.0, 40.0, 30.0],
                [15.0, 25.0, 20.0],
            ],
            dtype=float,
        )

        # Define layers and their transformations
        layer_names = ["Conv", "BatchNorm", "ReLU", "Conv", "BatchNorm"]
        layer_colors = [GREEN, TEAL, ORANGE, GREEN, TEAL]

        # Store current values
        current_values = input_values.copy()

        # Process each layer one at a time
        for idx, (layer_name, layer_color) in enumerate(zip(layer_names, layer_colors)):
            # Clear screen except title
            if idx > 0:
                self.play(
                    *[FadeOut(mob) for mob in self.mobjects if mob != title],
                    run_time=0.4,
                )
                self.wait(0.2)

            # Show layer indicator
            layer_indicator = Text(
                f"Layer {idx + 1}: {layer_name}", font_size=30, color=layer_color
            ).next_to(title, DOWN, buff=0.5)
            self.play(Write(layer_indicator, run_time=0.5))
            self.wait(0.5)

            # Position for input grid (left side)
            input_pos = LEFT * 4.5
            input_grid = create_grid(
                current_values, input_pos, BLUE if idx == 0 else layer_colors[idx - 1]
            )
            input_label = Text(
                "Input" if idx == 0 else f"From {layer_names[idx-1]}", font_size=18
            ).next_to(input_grid, DOWN, buff=0.2)

            self.play(FadeIn(input_grid, input_label, run_time=0.6))
            self.wait(0.3)

            # Position for output grid (right side)
            output_pos = RIGHT * 3.5

            # Apply transformation and create formula
            if layer_name == "Conv":
                formula = VGroup(
                    Text(layer_name, font_size=18, color=layer_color, weight=BOLD),
                    Text("x × 0.8 + 5", font_size=18, color=layer_color),
                ).arrange(DOWN, buff=0.1)
                new_values = current_values * 0.8 + 5
            elif layer_name == "BN":
                mean_val = np.mean(current_values)
                std_val = np.std(current_values)
                formula = VGroup(
                    Text(layer_name, font_size=18, color=layer_color, weight=BOLD),
                    Text("(x - μ) / σ", font_size=18, color=layer_color),
                    Text(
                        f"μ={mean_val:.1f}, σ={std_val:.1f}",
                        font_size=11,
                        color=layer_color,
                    ),
                ).arrange(DOWN, buff=0.1)
                new_values = (current_values - mean_val) / (std_val + 1e-5) * 8 + 25
            elif layer_name == "ReLU":
                formula = VGroup(
                    Text(layer_name, font_size=18, color=layer_color, weight=BOLD),
                    Text("max(0, x)", font_size=18, color=layer_color),
                ).arrange(DOWN, buff=0.1)
                new_values = np.maximum(current_values, 0)

            # Create single horizontal arrow from input to output
            start_point = input_grid.get_right()
            start_point[1] = input_grid.get_center()[1]  # force horizontal level
            end_point = np.array([output_pos[0] - 1.0, start_point[1], 0])
            arrow = Arrow(
                start=start_point + RIGHT * 0.1,
                end=end_point,
                buff=0.1,
                color=layer_color,
                stroke_width=3,
            )

            # Position formula above the arrow
            arrow_center = (arrow.get_start() + arrow.get_end()) / 2
            formula.move_to(arrow_center + UP * 0.8)

            # Create the arrow and formula
            self.play(Create(arrow, run_time=0.6))
            self.play(Write(formula, run_time=0.7))
            self.wait(0.4)

            # Create output grid (right side)
            output_grid = create_grid(new_values, output_pos, layer_color)
            output_label = Text(
                f"After {layer_name}", font_size=18, color=layer_color
            ).next_to(output_grid, DOWN, buff=0.2)

            self.play(FadeIn(output_grid, output_label, run_time=0.7))
            self.wait(0.8)

            # Update current values for next iteration
            current_values = new_values.copy()

        # Store final f(x) values
        fx_values = current_values.copy()

        # Now show the skip connection and final addition
        self.wait(0.5)

        # Clear screen except title
        self.play(
            *[FadeOut(mob) for mob in self.mobjects if mob != title], run_time=0.5
        )
        self.wait(0.3)

        # Show final composition: x + f(x) = y
        subtitle = Text("Final Step: Residual Connection", font_size=28).next_to(
            title, DOWN, buff=0.3
        )
        self.play(Write(subtitle, run_time=0.7))
        self.wait(0.4)

        # Position for final display - horizontal layout
        input_final_pos = LEFT * 5
        plus_pos = LEFT * 2.5
        fx_final_pos = ORIGIN
        equals_pos = RIGHT * 2.5
        output_final_pos = RIGHT * 4.5

        # Show input grid (original x)
        input_grid_final = create_grid(input_values, input_final_pos, BLUE)
        input_label_final = Text("x (original)", font_size=14).next_to(
            input_grid_final, DOWN, buff=0.2
        )

        # Plus sign
        plus_sign = Text("+", font_size=40).move_to(plus_pos)

        # Show f(x) grid (result after all 5 layers)
        fx_grid = create_grid(fx_values, fx_final_pos, PURPLE)
        fx_label = Text("f(x) (all layers)", font_size=14).next_to(
            fx_grid, DOWN, buff=0.2
        )

        # Equals sign
        equals_sign = Text("=", font_size=40).move_to(equals_pos)

        # Show output grid (element-wise addition)
        output_values = input_values + fx_values
        output_grid = create_grid(output_values, output_final_pos, RED)
        output_label = Text("y (output)", font_size=14).next_to(
            output_grid, DOWN, buff=0.2
        )

        # Animate the final equation
        self.play(FadeIn(input_grid_final, input_label_final, run_time=0.6))
        self.wait(0.3)
        self.play(Write(plus_sign, run_time=0.4))
        self.wait(0.2)
        self.play(FadeIn(fx_grid, fx_label, run_time=0.6))
        self.wait(0.3)
        self.play(Write(equals_sign, run_time=0.4))
        self.wait(0.2)
        self.play(FadeIn(output_grid, output_label, run_time=0.7))
        self.wait(0.5)

        # Show skip connection arrow
        skip_arrow = CurvedArrow(
            start_point=input_grid_final.get_bottom() + DOWN * 0.4,
            end_point=output_grid.get_bottom() + DOWN * 0.4,
            color=YELLOW,
            stroke_width=5,
        )
        skip_label = Text("Skip Connection", font_size=16, color=YELLOW).next_to(
            skip_arrow, DOWN, buff=0.1
        )

        self.play(Create(skip_arrow, run_time=1.0))
        self.play(Write(skip_label, run_time=0.5))
        self.wait(0.5)

        # Add calculation example
        example_pos = DOWN * 2.2
        example_text = (
            VGroup(
                Text("Example: center cell calculation", font_size=14),
                Text(f"x[1,1] = {input_values[1,1]:.1f}", font_size=13, color=BLUE),
                Text(f"f(x)[1,1] = {fx_values[1,1]:.1f}", font_size=13, color=PURPLE),
                Text(
                    f"y[1,1] = {input_values[1,1]:.1f} + {fx_values[1,1]:.1f} = {output_values[1,1]:.1f}",
                    font_size=13,
                    color=RED,
                ),
            )
            .arrange(DOWN, aligned_edge=LEFT, buff=0.12)
            .move_to(example_pos)
        )

        self.play(Write(example_text, run_time=1.0))
        self.wait(2.0)
