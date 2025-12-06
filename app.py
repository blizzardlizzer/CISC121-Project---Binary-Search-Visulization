import gradio as gr
import time
import random
from typing import List, Tuple


#checks inputs and converts to the same format each time to avoid errors
def try_parse_number(s: str):
    s = s.strip()
    try:
        return int(s)
    except:
        try:
            return float(s)
        except:
            raise


def render_array_frame(arr, left, right, mid, message):
    html = "<div style='font-family:monospace;font-size:20px;margin-top:10px;'>"
    for i, v in enumerate(arr):
    # Determine color based on position
        color = "#000000"
        if left <= i <= right:
            color = "#c8dcf0"
        if i == mid:
            color = "#ffb700"
        if i == left:
            color = "#008cff"
        if i == right:
            color = "#ff0000"
        # created the visuals blocks for each element
        html += f"""
        <div style="
            display:inline-block;
            padding:10px 14px;
            margin:4px;
            border-radius:6px;
            border:2px solid #bdbdbd;
            color:black;
            background:{color};
            text-align:center;
            min-width:30px;
        ">{v}</div>
        """
    # creates pointers for each block to help with visualization
    pointer_row = "<div style='font-size:16px;'>"
    for i in range(len(arr)):
        label = ""
        if i == left: label += "L"
        if i == mid: label += " M"
        if i == right: label += " R"
        pointer_row += f"<div style='display:inline-block; width:65px; text-align:center;'>{label}</div>"
    pointer_row += "</div>"
    html += pointer_row
    html += f"<div style='margin-top:10px;font-size:18px;'>{message}</div>"
    return html


def build_binary_search_steps(arr_text: str, target_value: float) -> Tuple[str, int]:
    try:
        parts = [p.strip() for p in arr_text.split(",") if p.strip() != ""]
        arr: List[float] = [try_parse_number(p) for p in parts]
    except:
        return "<div style='color:red;'>Invalid array format.</div>", -1

    if any(arr[i] > arr[i+1] for i in range(len(arr)-1)):
        return "<div style='color:red;'>Array must be sorted.</div>", -1

    left, right = 0, len(arr) - 1
    step = 1
    found_index = -1
    html_parts = ["<div style='font-family:monospace;'>"]
    html_parts.append(f"<h3>Binary Search Steps (target = {target_value})</h3>")

    #regular binary search steps but with added steo by step visualization steps basedon the pointers
    while left <= right:
        mid = left + (right - left) // 2
        html_parts.append(render_array_frame(arr, left, right, mid, f"Step {step}: left={left}, right={right}, mid={mid}"))

        if arr[mid] == target_value:
            html_parts.append(f"<div style='color:green;font-weight:600;'>Found target: arr[{mid}] == {target_value}</div>")
            found_index = mid
            break
        elif arr[mid] < target_value:
            left = mid + 1
        else:
            right = mid - 1
        step += 1

    if found_index == -1:
        html_parts.append(f"<div style='margin-top:8px;color:#a00;font-weight:600;'>Target {target_value} not found.</div>")

    html_parts.append("</div>")
    return "\n".join(html_parts), found_index


def animated_binary_search(arr_text, target, speed, use_random=False):
    random_target_display = ""
    # checks if the random array check box is checked and then generates the array and target
    if use_random:
        arr = sorted(random.randint(0, 100) for _ in range(50))
        target = random.choice(arr)
        arr_text = ", ".join(map(str, arr))
        random_target_display = str(target)
    else:
        try:
            arr = [int(x.strip()) for x in arr_text.split(",") if x.strip() != ""]
        except:
            yield "<div style='color:red;'>Invalid input array.</div>", "Invalid input", ""
            return

    arr.sort()
    delay = max(0.05, 1.0 - speed)
    left, right = 0, len(arr) - 1
    yield render_array_frame(arr, left, right, -1, "Starting binary search..."), "Starting...", random_target_display
    time.sleep(delay)

    #binary search algorithm with small tweaks that allow for visualization with each step
    while left <= right:
        mid = left + (right - left) // 2
        yield render_array_frame(arr, left, right, mid, f"Checking mid = {mid}"), f"Checking index {mid}", random_target_display
        time.sleep(delay)

        if arr[mid] == target:
            yield render_array_frame(arr, left, right, mid, f"Found value {target} at index {mid}!"), f"Found at index {mid}", random_target_display
            return
        elif arr[mid] < target:
            yield render_array_frame(arr, left, right, mid, f"{arr[mid]} < {target} → Move left pointer right"), "Adjusting left", random_target_display
            left = mid + 1
        else:
            yield render_array_frame(arr, left, right, mid, f"{arr[mid]} > {target} → Move right pointer left"), "Adjusting right", random_target_display
            right = mid - 1
        time.sleep(delay)

    yield render_array_frame(arr, -1, -1, -1, f"Value {target} not found."), "Not found", random_target_display

# Gradio Interface
with gr.Blocks() as demo:
    gr.Markdown("## Binary Search Visualization")
    with gr.Tabs():
        with gr.TabItem("Static Steps"):
            # visuals for step by step
            arr_input1 = gr.Textbox(label="Sorted Array", value="Enter Array Here(Comma seperated) ex. 1,2,3,4,5")
            target_input1 = gr.Number(label="Target", value="Enter Target Here")
            static_out = gr.HTML(label="Step-by-step Visualization")
            gr.Button("Run").click(build_binary_search_steps, inputs=[arr_input1, target_input1], outputs=[static_out])

        #visuals for animated steps
        with gr.TabItem("Animated Steps"):
            arr_input2 = gr.Textbox(label="Sorted Array", value="Enter Array Here(Comma Seperated)")
            target_input2 = gr.Number(label="Target", value="Enter Target Here")
            speed_input = gr.Slider(0, 1, value=0.5, label="Speed (0=fast,1=slow)")
            use_random_input = gr.Checkbox(label="Use Random Array")
            anim_out = gr.HTML(label="Animated Steps")
            status_out = gr.Textbox(label="Status")
            random_target_out = gr.Textbox(label="Random Target")
            gr.Button("Run Animation").click(animated_binary_search, 
                                             inputs=[arr_input2, target_input2, speed_input, use_random_input], 
                                             outputs=[anim_out, status_out, random_target_out])

demo.launch()
