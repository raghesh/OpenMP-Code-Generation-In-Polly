define i32 @main() nounwind {
entry:
  %retval = alloca i32, align 4
  %i = alloca i32, align 4
  %j = alloca i32, align 4
  store i32 0, i32* %retval
  store i32 0, i32* %i, align 4
  br label %for.cond

for.cond:
  %tmp = load i32* %i, align 4
  %cmp = icmp slt i32 %tmp, 1024
  br i1 %cmp, label %for.body,
              label %for.end12

for.body:
  store i32 0, i32* %j, align 4
  br label %for.cond1

for.cond1:
  %tmp2 = load i32* %j, align 4
  %cmp3 = icmp slt i32 %tmp2, 5000000
  br i1 %cmp3, label %for.body4,
               label %for.end
