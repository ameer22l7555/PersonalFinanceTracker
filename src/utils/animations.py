class ValueAnimator:
    @staticmethod
    def animate_value_change(root, label, start_val, end_val, duration=500, steps=20):
        """Animate value change in labels"""
        increment = (end_val - start_val) / steps
        
        def update_value(current_step):
            if current_step <= steps:
                current_val = start_val + (increment * current_step)
                label.configure(text=f"${current_val:.2f}")
                root.after(duration // steps, update_value, current_step + 1)
        
        update_value(0) 