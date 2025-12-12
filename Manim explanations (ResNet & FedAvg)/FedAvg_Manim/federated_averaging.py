from manim import *

class FederatedAveraging(Scene):
    def construct(self):
        # Title
        title = Text("Federated Averaging", font_size=48, weight=BOLD)
        subtitle = Text("Federated Learning Algorithm", font_size=24)
        subtitle.next_to(title, DOWN)
        
        self.play(Write(title))
        self.play(FadeIn(subtitle))
        self.wait(1)
        self.play(FadeOut(title), FadeOut(subtitle))
        
        # --- Intro: What is FedAvg and why? ---

        fedavg_title = Text("What is Federated Averaging (FedAvg)?",
                            font_size=30, weight=BOLD, color=YELLOW)
        fedavg_title.to_edge(UP)

        fedavg_explanation = VGroup(
            Text("FedAvg is a federated learning algorithm that trains a shared ", font_size=24),
            Text("model on many clients without moving their raw data to the server.", font_size=24),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        fedavg_explanation.next_to(fedavg_title, DOWN, buff=0.5)

        importance_title = Text("Why is it important?", font_size=26, weight=BOLD, color=GOLD)
        importance_title.next_to(fedavg_explanation, DOWN, buff=0.6, aligned_edge=LEFT)

        importance_points = VGroup(
            Text("✓ Privacy: Data never leaves client devices", font_size=22),
            Text("✓ Efficiency: Only model updates transmitted", font_size=22),
            Text("✓ Scalability: Works with millions of clients", font_size=22)
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        importance_points.next_to(importance_title, DOWN, buff=0.3, aligned_edge=LEFT)

        intro_group = VGroup(
            fedavg_title, fedavg_explanation,
            importance_title, importance_points
        )

        self.play(Write(fedavg_title))
        self.play(LaggedStart(*[FadeIn(line) for line in fedavg_explanation], lag_ratio=0.15))
        self.play(FadeIn(importance_title))
        self.play(LaggedStart(*[FadeIn(pt) for pt in importance_points], lag_ratio=0.15))
        self.wait(3)
        self.play(FadeOut(intro_group))

        # --- Key parameters before the round ---

        params_title = Text("Key FedAvg Parameters", font_size=28, weight=BOLD, color=YELLOW)
        params_title.to_edge(UP)

        params_list = VGroup(
            MathTex("C", " : ", r"\text{fraction of clients selected per round}", font_size=24),
            MathTex("E", " : ", r"\text{local epochs per client}", font_size=24),
            MathTex(r"\eta", " : ", r"\text{learning rate}", font_size=24),
            MathTex("T", " : ", r"\text{number of communication rounds}", font_size=24),
        ).arrange(DOWN, buff=0.35, aligned_edge=LEFT)

        for item in params_list:
            item[0].set_color(YELLOW)

        params_list.next_to(params_title, DOWN, buff=0.5)

        self.play(Write(params_title))
        self.play(LaggedStart(*[Write(item) for item in params_list], lag_ratio=0.2))
        self.wait(3)
        self.play(FadeOut(params_title), FadeOut(params_list))

        # Scene 1: Setup - Server and Clients
        server = Circle(radius=0.5, color=BLUE, fill_opacity=0.8)
        server_label = Text("Server", font_size=20).next_to(server, UP, buff=0.2)
        server_group = VGroup(server, server_label).to_edge(UP)
        
        # Create 5 clients to show selection
        clients = VGroup()
        client_labels = VGroup()
        for i in range(5):
            client = Circle(radius=0.35, color=GREEN, fill_opacity=0.6)
            label = Text(f"Client {i+1}", font_size=16)
            label.next_to(client, DOWN, buff=0.15)
            clients.add(client)
            client_labels.add(label)
        
        clients_with_labels = VGroup(*[VGroup(clients[i], client_labels[i]) for i in range(5)])
        clients_with_labels.arrange(RIGHT, buff=0.8).shift(DOWN * 1.5)
        
        self.play(FadeIn(server_group))
        self.play(FadeIn(clients_with_labels))
        self.wait(1)
        
        # Explain client selection - put on LEFT side
        selection_title = Text("Client Selection", font_size=24, weight=BOLD, color=YELLOW)
        selection_title.to_edge(LEFT).shift(RIGHT * 0.2 + UP * 3)
        
        selection_methods = VGroup(
            Text("• Random: select fraction C of clients", font_size=16),
            Text("• Round Robin: cycle through clients", font_size=16),
            Text("• Importance-based:by data quality/quantity", font_size=16),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        selection_methods.next_to(selection_title, DOWN, buff=0.4, aligned_edge=LEFT)
        
        selection_box = VGroup(selection_title, selection_methods)
        
        self.play(Write(selection_title))
        self.play(LaggedStart(*[FadeIn(item) for item in selection_methods], lag_ratio=0.2))
        self.wait(3)
        self.play(FadeOut(selection_box))
        
        # Show client fraction C - put on LEFT side
        fraction_title = Text("Client Fraction", font_size=22, weight=BOLD, color=YELLOW)
        fraction_title.to_edge(LEFT).shift(RIGHT * 0.2 + UP * 3)
        
        fraction_formula = MathTex("C = 0.6", font_size=26, color=YELLOW)
        fraction_formula.next_to(fraction_title, DOWN, buff=0.3, aligned_edge=LEFT)
        
        fraction_explanation = Text("(60% selected per round)", font_size=16, color=WHITE)
        fraction_explanation.next_to(fraction_formula, DOWN, buff=0.3, aligned_edge=LEFT)
        
        fraction_group = VGroup(fraction_title, fraction_formula, fraction_explanation)
        
        self.play(Write(fraction_group))
        self.wait(1.5)
        
        # Highlight selected clients (3 out of 5 = 60%)
        selected_indices = [0, 2, 3]
        for i in selected_indices:
            self.play(clients[i].animate.set_color(ORANGE).scale(1.15), run_time=0.3)
        
        # Dim non-selected clients
        for i in range(5):
            if i not in selected_indices:
                self.play(clients[i].animate.set_opacity(0.3), 
                         client_labels[i].animate.set_opacity(0.3), run_time=0.3)
        
        self.wait(1)
        self.play(FadeOut(fraction_group))
        
        # Focus on selected clients only
        selected_clients = VGroup(*[clients[i] for i in selected_indices])
        selected_labels = VGroup(*[client_labels[i] for i in selected_indices])
        
        # Scene 2: Initial model distribution
        init_text1 = Text("Initialize global model ", font_size=22)
        init_text2 = Text("at round", font_size=22)
        init_formula = MathTex("t = 0", font_size=26)
        init_model = MathTex("w^{0}", font_size=32, color=YELLOW)
        init_group = VGroup(init_text1, init_model, init_text2, init_formula).arrange(RIGHT, buff=0.3)
        init_group.to_edge(DOWN)
        
        self.play(Write(init_group))
        self.wait(0.5)
        
        # Show arrows from server to selected clients only
        arrows_down = VGroup()
        for i in selected_indices:
            arrow = Arrow(server.get_bottom(), clients[i].get_top(), 
                         color=YELLOW, stroke_width=4)
            arrows_down.add(arrow)
        
        self.play(LaggedStart(*[GrowArrow(arrow) for arrow in arrows_down], 
                             lag_ratio=0.3))
        self.wait(0.5)
        self.play(FadeOut(arrows_down), FadeOut(init_group))
        
        # Explain w^t notation when first introduced
        w_explanation = VGroup(
            MathTex("w^{t}", font_size=32, color=YELLOW),
            Text(" = global model weights at round ", font_size=20),
            MathTex("t", font_size=24, color=YELLOW)
        ).arrange(RIGHT, buff=0.2)
        w_explanation.to_edge(DOWN)
        self.play(Write(w_explanation))
        self.wait(2)
        self.play(FadeOut(w_explanation))
        
        # Scene 3: Local epochs explanation - put on LEFT side
        epochs_title = Text("Local Training", font_size=22, weight=BOLD, color=YELLOW)
        epochs_title.to_edge(LEFT).shift(RIGHT * 0.2 + UP * 3)
        
        epochs_notation = MathTex("E", " = ", font_size=22)
        epochs_notation[0].set_color(YELLOW)
        epochs_notation.next_to(epochs_title, DOWN, buff=0.6, aligned_edge=LEFT)
        
        epochs_explanation = VGroup(
            Text("\n\nnumber of local training epochs", font_size=16, color=WHITE),
            Text("Each client trains for E epochs on", font_size=16, color=WHITE),
            Text("their local data", font_size=16, color=WHITE)
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        epochs_explanation.next_to(epochs_notation, RIGHT, buff=0.3)
        
        epochs_group = VGroup(epochs_title, epochs_notation, epochs_explanation)
        
        self.play(Write(epochs_title))
        self.play(Write(epochs_notation), Write(epochs_explanation))
        self.wait(2.5)
        self.play(FadeOut(epochs_group))
        
        # Show data and training on selected clients
        training_text = Text("Training on Local Data (E epochs)", font_size=22)
        training_text.to_edge(DOWN)
        self.play(Write(training_text))
        
        data_icons = VGroup()
        for i in selected_indices:
            data = VGroup(*[
                Dot(radius=0.04, color=RED).shift(UP*0.08*j + LEFT*0.08*k)
                for j in range(3) for k in range(3)
            ])
            data.scale(0.5).move_to(clients[i])
            data_icons.add(data)
        
        self.play(LaggedStart(*[FadeIn(icon) for icon in data_icons], 
                             lag_ratio=0.2))
        
        # Pulsing effect to show training over E epochs
        for _ in range(2):
            self.play(*[clients[i].animate.scale(1.15).set_color(RED) 
                       for i in selected_indices], run_time=0.4)
            self.play(*[clients[i].animate.scale(1/1.15).set_color(ORANGE) 
                       for i in selected_indices], run_time=0.4)
        
        self.wait(0.5)
        self.play(FadeOut(data_icons), FadeOut(training_text))
        
        # Scene 4: Show gradient computation with explanation - LEFT side
        gradient_title = Text("Gradient", font_size=24, weight=BOLD, color=YELLOW)
        gradient_title.to_edge(LEFT).shift(RIGHT * 0.5 + UP * 1.5)
        
        # Introduce F_k notation
        f_notation = MathTex(
            "F_{k}(w)", " = ",
            font_size=24
        )
        f_notation[0].set_color(YELLOW)
        f_notation.next_to(gradient_title, DOWN, buff=0.3, aligned_edge=LEFT)
        
        f_explanation = VGroup(
            Text("loss function on client k's local data", font_size=17, color=WHITE)
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        f_explanation.next_to(f_notation, RIGHT, buff=0.3)
        
        gradient_box = VGroup(gradient_title, f_notation, f_explanation)
        
        self.play(Write(gradient_title))
        self.play(Write(f_notation), Write(f_explanation))
        self.wait(2)
        self.play(FadeOut(gradient_box))
        
        # Show gradients
        gradient_text = Text("Compute Local Gradients", font_size=22)
        gradient_text.to_edge(DOWN)
        self.play(Write(gradient_text))
        
        gradients = VGroup()
        for idx, i in enumerate(selected_indices):
            gradient = MathTex(r"\nabla F_{k}(w^{t})", font_size=22)
            gradient.move_to(clients[i].get_center())  
            gradient.shift(DOWN * 0.05)                
            gradients.add(gradient)

        
        self.play(LaggedStart(*[Write(g) for g in gradients], lag_ratio=0.3))
        self.wait(1.5)
        self.play(FadeOut(gradient_text))
        
        # Scene 5: Update local models with learning rate explanation - LEFT side
        # Introduce eta when used
        eta_title = Text("Learning Rate", font_size=22, weight=BOLD, color=YELLOW)
        eta_title.to_edge(LEFT).shift(RIGHT * 0.5 + UP * 1.5)
        
        eta_notation = MathTex(
            r"\eta", " = ",
            font_size=24
        )
        eta_notation[0].set_color(YELLOW)
        eta_notation.next_to(eta_title, DOWN, buff=0.6, aligned_edge=LEFT)
        
        eta_explanation = VGroup(
            Text("controls step size of model updates", font_size=17, color=WHITE),
            Text("typical values: 0.01, 0.1, etc.", font_size=17, color=WHITE)
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        eta_explanation.next_to(eta_notation, RIGHT, buff=0.3)
        
        eta_box = VGroup(eta_title, eta_notation, eta_explanation)
        
        self.play(Write(eta_title))
        self.play(Write(eta_notation), Write(eta_explanation))
        self.wait(2)
        self.play(FadeOut(eta_box))
        
        # Show update formula - LEFT side
        update_title = Text("Local Update", font_size=22, weight=BOLD, color=YELLOW)
        update_title.to_edge(LEFT).shift(RIGHT * 0.5 + UP * 2)
        
        update_formula = MathTex(
            "w_{k}^{t+1}", " = ", "w^{t}", " - ", r"\eta", r"\nabla F_{k}(w^{t})",
            font_size=24
        )
        update_formula[0].set_color(YELLOW)
        update_formula[4].set_color(YELLOW)
        update_formula.next_to(update_title, DOWN, buff=0.4, aligned_edge=LEFT)
        
        update_group = VGroup(update_title, update_formula)
        
        self.play(Write(update_title))
        self.play(Write(update_formula))
        self.wait(2)
        
        # Introduce w_k notation - LEFT side  
        wk_explanation = VGroup(
            MathTex("w_{k}^{t+1}", " = ", font_size=20, color=YELLOW),
            Text("updated model for client k", font_size=17, color=WHITE)
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        wk_explanation.next_to(update_formula, DOWN, buff=0.4, aligned_edge=LEFT)
        self.play(FadeIn(wk_explanation))
        self.wait(1.5)
        self.play(FadeOut(wk_explanation))
        self.play(FadeOut(gradients))

        
        # Show updated models on selected clients
        updated_models = VGroup()
        for i in selected_indices:
            client_id = i + 1          # 1, 3, 4
            model = MathTex(f"w_{{{client_id}}}^{{t+1}}", font_size=26, color=YELLOW)
            model.move_to(clients[i])
            updated_models.add(model)
        
        self.play(LaggedStart(*[FadeIn(m) for m in updated_models], lag_ratio=0.2))
        self.wait(1)
        self.play(FadeOut(update_group))
        
        # Scene 6: Send updates back to server
        send_text = Text("Send Local Models to Server", font_size=22)
        send_text.to_edge(DOWN)
        self.play(Write(send_text))
        
        arrows_up = VGroup()
        for i in selected_indices:
            arrow = Arrow(clients[i].get_top(), server.get_bottom(), 
                         color=PURPLE, stroke_width=4)
            arrows_up.add(arrow)
        
        self.play(LaggedStart(*[GrowArrow(arrow) for arrow in arrows_up], 
                             lag_ratio=0.3))
        self.wait(0.5)
        self.play(FadeOut(arrows_up), FadeOut(send_text))
        
        # Scene 7: Server aggregation - LEFT side explanation
        agg_title = Text("Aggregation", font_size=22, weight=BOLD, color=YELLOW)
        agg_title.to_edge(LEFT).shift(RIGHT * 0.5 + UP * 2)
        self.play(Write(agg_title))
        
        # Move models to server
        self.play(*[model.animate.move_to(server).scale(0.6) 
                   for model in updated_models])
        self.wait(0.5)
        
        # Explain aggregation with proper notation - LEFT side
        nk_notation = MathTex(
            "n_{k}", " = ",
            font_size=20
        )
        nk_notation[0].set_color(YELLOW)
        nk_notation.next_to(agg_title, DOWN, buff=0.4, aligned_edge=LEFT)
        
        nk_text = VGroup(
            Text("# of samples on client k", font_size=17, color=WHITE),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        nk_text.next_to(nk_notation, RIGHT, buff=0.2)
        
        n_notation = MathTex(
            "n", " = ", r"\sum_{k} n_{k}",
            font_size=20
        )
        n_notation[0].set_color(YELLOW)
        n_notation[2].set_color(YELLOW)
        n_notation.next_to(nk_notation, DOWN, buff=0.3, aligned_edge=LEFT)
        
        n_text = Text("total samples", font_size=17, color=WHITE)
        n_text.next_to(n_notation, DOWN, buff=0.2, aligned_edge=LEFT)
        
        agg_explanation = VGroup(agg_title, nk_notation, nk_text, n_notation, n_text)
        
        self.play(Write(nk_notation), Write(nk_text))
        self.play(Write(n_notation), Write(n_text))
        self.wait(3)
        self.play(FadeOut(agg_explanation))
        
        # Show averaging formula - LEFT side
        avg_title = Text("FedAvg Formula", font_size=22, weight=BOLD, color=YELLOW)
        avg_title.to_edge(LEFT).shift(RIGHT * 0.5 + UP * 3)
        
        avg_formula = MathTex(
            "w^{t+1}", " = ", 
            r"\sum_{k=1}^{K}", 
            r"\frac{n_{k}}{n}", 
            "w_{k}^{t+1}",
            font_size=26
        )
        avg_formula[0].set_color(GOLD)
        avg_formula[3].set_color(YELLOW)
        avg_formula[4].set_color(YELLOW)
        avg_formula.next_to(avg_title, DOWN, buff=0.4, aligned_edge=LEFT)
        frac_explanation = VGroup(
            Text("n_k = number of samples on client k", font_size=16, color=GRAY),
            Text("n   = total samples across all selected clients", font_size=16, color=GRAY),
            Text("n_k / n = weight of client k in the average", font_size=16, color=WHITE)
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT)

        frac_explanation.next_to(avg_formula, DOWN, buff=0.3, aligned_edge=LEFT)

        avg_group = VGroup(avg_title, avg_formula, frac_explanation)

        self.play(Write(avg_title))
        self.play(Write(avg_formula))
        self.play(LaggedStart(*[Write(line) for line in frac_explanation], lag_ratio=0.15))
        self.wait(3)
        self.play(FadeOut(frac_explanation), FadeOut(avg_title), FadeOut(avg_formula))
    

        
        # Show final averaged model
        self.play(FadeOut(updated_models))
        final_model = MathTex("w^{t+1}", font_size=36, color=GOLD)
        final_model.move_to(server)
        self.play(FadeIn(final_model), server.animate.set_color(GOLD))
        self.wait(1.5)
    
        
        # Scene 8: Iteration
        repeat_text = Text("Repeat for T communication rounds/until convergence", font_size=25, weight=BOLD)
        repeat_text.to_edge(DOWN)
        self.play(Write(repeat_text))
        self.wait(1.5)
        self.play(FadeOut(repeat_text))
        
        # Reset client appearance for next round
        for i in range(5):
            if i in selected_indices:
                self.play(clients[i].animate.set_color(GREEN).scale(1/1.15).set_opacity(1),
                         client_labels[i].animate.set_opacity(1), run_time=0.2)
            else:
                self.play(clients[i].animate.set_opacity(1),
                         client_labels[i].animate.set_opacity(1), run_time=0.2)
        
        # Show a couple more rounds with different client selection
        for round_num in range(2, 4):
            round_label = Text(f"Round t = {round_num}", font_size=28, color=YELLOW)
            round_label.to_edge(UP, buff=0.5).shift(RIGHT * 3)
            self.play(FadeIn(round_label))
            
            # Select different clients
            new_selected = [1, 2, 4] if round_num == 2 else [0, 1, 3]
            for i in new_selected:
                self.play(clients[i].animate.set_color(ORANGE).scale(1.1), run_time=0.2)
            
            # Quick arrows
            arrows_d = VGroup(*[Arrow(server.get_bottom(), clients[i].get_top(), 
                                     color=YELLOW, stroke_width=3) 
                              for i in new_selected])
            self.play(LaggedStart(*[GrowArrow(arrow) for arrow in arrows_d], 
                                lag_ratio=0.1), run_time=0.4)
            self.play(FadeOut(arrows_d))
            
            arrows_u = VGroup(*[Arrow(clients[i].get_top(), server.get_bottom(), 
                                     color=PURPLE, stroke_width=3) 
                              for i in new_selected])
            self.play(LaggedStart(*[GrowArrow(arrow) for arrow in arrows_u], 
                                lag_ratio=0.1), run_time=0.4)
            self.play(FadeOut(arrows_u), FadeOut(round_label))
            
            # Reset colors
            for i in new_selected:
                self.play(clients[i].animate.set_color(GREEN).scale(1/1.1), run_time=0.2)
        
        # Clear scene for summary
        self.play(FadeOut(server_group), FadeOut(clients_with_labels), FadeOut(final_model))
        
        # Ending Summary

        end_title = Text("What FedAvg Achieves", font_size=32, weight=BOLD, color=YELLOW)
        end_title.to_edge(UP)

        end_points = VGroup(
            Text("Combines many local models into one global model", font_size=24),
            Text("Learns from distributed data while keeping it on devices", font_size=24),
            Text("Improves the model over T communication rounds", font_size=24),
        ).arrange(DOWN, buff=0.35, aligned_edge=LEFT)

        end_points.next_to(end_title, DOWN, buff=0.6)

        self.play(Write(end_title))
        self.play(LaggedStart(*[FadeIn(p) for p in end_points], lag_ratio=0.2))
        self.wait(4)
        self.play(FadeOut(end_title), FadeOut(end_points))


