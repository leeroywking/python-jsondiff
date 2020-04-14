Have you ever wished you could copy and paste a JSON diff tool into a remote server so you could just easily diff two different large JSON objects which perhaps had been reordered?

I ran into an issue where I needed to diff two different very large JSON files. A traditional linux diff wasn't helping since the JSON had been reordered slightly so the linux diff was massive and when I wanted to actually see how the changed lines/values were nested I ended up doing a lot of scrolling and generally it was a very unsatisfactory experience.

So rather than resigning myself to a fate of editing JSON by hand I wanted to brush off some DSA fundamentals and learn a bit of Python. I wrote two solutions which are nearly identical but the iterative solution puts the items into a "stack" (I used a Python list) rather than recursively navigating the entire JSON object in a single call. This could be more performant if you can find even larger JSON objects than I tested with, in practice they seemed to be about the same speed for me.

To use this the syntax is python3 json_diff_recursive.py path/to/file1.json path/to/file2.json
