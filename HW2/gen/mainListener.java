// Generated from C:/Users/black/compiler_design_fall_2023/HW2/main.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link mainParser}.
 */
public interface mainListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link mainParser#equation}.
	 * @param ctx the parse tree
	 */
	void enterEquation(mainParser.EquationContext ctx);
	/**
	 * Exit a parse tree produced by {@link mainParser#equation}.
	 * @param ctx the parse tree
	 */
	void exitEquation(mainParser.EquationContext ctx);
	/**
	 * Enter a parse tree produced by {@link mainParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterExpression(mainParser.ExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link mainParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitExpression(mainParser.ExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link mainParser#multiplyingExpression}.
	 * @param ctx the parse tree
	 */
	void enterMultiplyingExpression(mainParser.MultiplyingExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link mainParser#multiplyingExpression}.
	 * @param ctx the parse tree
	 */
	void exitMultiplyingExpression(mainParser.MultiplyingExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link mainParser#powExpression}.
	 * @param ctx the parse tree
	 */
	void enterPowExpression(mainParser.PowExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link mainParser#powExpression}.
	 * @param ctx the parse tree
	 */
	void exitPowExpression(mainParser.PowExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link mainParser#signedAtom}.
	 * @param ctx the parse tree
	 */
	void enterSignedAtom(mainParser.SignedAtomContext ctx);
	/**
	 * Exit a parse tree produced by {@link mainParser#signedAtom}.
	 * @param ctx the parse tree
	 */
	void exitSignedAtom(mainParser.SignedAtomContext ctx);
	/**
	 * Enter a parse tree produced by {@link mainParser#atom}.
	 * @param ctx the parse tree
	 */
	void enterAtom(mainParser.AtomContext ctx);
	/**
	 * Exit a parse tree produced by {@link mainParser#atom}.
	 * @param ctx the parse tree
	 */
	void exitAtom(mainParser.AtomContext ctx);
	/**
	 * Enter a parse tree produced by {@link mainParser#scientific}.
	 * @param ctx the parse tree
	 */
	void enterScientific(mainParser.ScientificContext ctx);
	/**
	 * Exit a parse tree produced by {@link mainParser#scientific}.
	 * @param ctx the parse tree
	 */
	void exitScientific(mainParser.ScientificContext ctx);
	/**
	 * Enter a parse tree produced by {@link mainParser#constant}.
	 * @param ctx the parse tree
	 */
	void enterConstant(mainParser.ConstantContext ctx);
	/**
	 * Exit a parse tree produced by {@link mainParser#constant}.
	 * @param ctx the parse tree
	 */
	void exitConstant(mainParser.ConstantContext ctx);
	/**
	 * Enter a parse tree produced by {@link mainParser#variable}.
	 * @param ctx the parse tree
	 */
	void enterVariable(mainParser.VariableContext ctx);
	/**
	 * Exit a parse tree produced by {@link mainParser#variable}.
	 * @param ctx the parse tree
	 */
	void exitVariable(mainParser.VariableContext ctx);
	/**
	 * Enter a parse tree produced by {@link mainParser#func_}.
	 * @param ctx the parse tree
	 */
	void enterFunc_(mainParser.Func_Context ctx);
	/**
	 * Exit a parse tree produced by {@link mainParser#func_}.
	 * @param ctx the parse tree
	 */
	void exitFunc_(mainParser.Func_Context ctx);
	/**
	 * Enter a parse tree produced by {@link mainParser#funcname}.
	 * @param ctx the parse tree
	 */
	void enterFuncname(mainParser.FuncnameContext ctx);
	/**
	 * Exit a parse tree produced by {@link mainParser#funcname}.
	 * @param ctx the parse tree
	 */
	void exitFuncname(mainParser.FuncnameContext ctx);
	/**
	 * Enter a parse tree produced by {@link mainParser#relop}.
	 * @param ctx the parse tree
	 */
	void enterRelop(mainParser.RelopContext ctx);
	/**
	 * Exit a parse tree produced by {@link mainParser#relop}.
	 * @param ctx the parse tree
	 */
	void exitRelop(mainParser.RelopContext ctx);
}