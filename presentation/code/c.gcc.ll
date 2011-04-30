define i32 @main() nounwind {
entry:
  %retval = alloca i32 
  %i = alloca i32
  %j = alloca i32 
  %"alloca point" = bitcast i32 0 to i32
  call void 
       @GOMP_parallel_loop_runtime_start(
       void (i8*)* @main.omp_fn.0,
       i8* null, i32 0, i32 0,
       i32 1024, i32 1) nounwind
  call void 
       @main.omp_fn.0(i8* null) nounwind
  call void 
       @GOMP_parallel_end() nounwind
  br label %return
`
return:                                           ; preds = %entry
  %retval1 = load i32* %retval                    ; <i32> [#uses=1]
  ret i32 %retval1
}
